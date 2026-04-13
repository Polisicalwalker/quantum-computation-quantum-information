#!/usr/bin/env python3
"""
Generate solutions.md for Nielsen & Chuang Chapter 3 exercises/problems
using the ZhipuAI GLM-5.1 model.

Features:
  - Reads exercises_raw.json (pre-extracted from the PDF)
  - Falls back to raw text files if JSON is missing
  - Calls ZhipuAI with rate-limit handling (429 / 1302 errors)
  - Mandatory 3-second delay between API calls
  - Append-only writes to solutions.md so progress is never lost
  - Skips already-completed exercises on restart
"""

import json
import os
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# ZhipuAI SDK – reads ZHIPUAI_API_KEY from env automatically
# ---------------------------------------------------------------------------
from zhipuai import ZhipuAI

client = ZhipuAI()  # uses os.environ.get('ZHIPUAI_API_KEY')

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
JSON_PATH = SCRIPT_DIR / "exercises_raw.json"
TXT_PATH = SCRIPT_DIR / "pymupdf_extract.txt"
FALLBACK_TXT = SCRIPT_DIR / "full_text.txt"
OUTPUT_PATH = SCRIPT_DIR / "solutions.md"

MODEL = "glm-5.1"          # ZhipuAI model name
MAX_RETRIES = 5               # max consecutive rate-limit retries per call
RETRY_DELAY = 3              # seconds to wait on 429 / 1302
INTER_CALL_DELAY = 0.5          # mandatory delay between successful calls

# ---------------------------------------------------------------------------
# Exercise extraction from raw text (fallback when JSON is absent)
# ---------------------------------------------------------------------------
def extract_exercises_from_text(text: str) -> list[dict]:
    """Split text into exercise/problem blocks using regex."""
    # Find all markers like "Exercise 3.X:" or "Problem 3.X:"
    marker_re = re.compile(r'(Exercise|Problem)\s+3\.(\d+)\s*:', re.IGNORECASE)
    markers = []
    for m in marker_re.finditer(text):
        markers.append({
            "type": m.group(1).capitalize(),
            "number": int(m.group(2)),
            "start": m.start(),
            "full_match": m.group(0),
        })

    exercises = []
    for i, marker in enumerate(markers):
        end = markers[i + 1]["start"] if i + 1 < len(markers) else len(text)
        block = text[marker["start"]:end].strip()
        # grab ~600 chars of context before the exercise
        ctx_start = max(0, marker["start"] - 600)
        context = text[ctx_start:marker["start"]].strip()
        exercises.append({
            "type": marker["type"],
            "number": marker["number"],
            "title": marker["full_match"],
            "text": block,
            "context": context,
        })
    return exercises


def load_exercises() -> list[dict]:
    """Load exercises from JSON, or fall back to raw text extraction."""
    if JSON_PATH.exists():
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"[INFO] Loaded {len(data)} exercises from {JSON_PATH.name}")
        return data

    # Try raw text files
    for txt_file in [TXT_PATH, FALLBACK_TXT]:
        if txt_file.exists():
            with open(txt_file, "r", encoding="utf-8") as f:
                text = f.read()
            exercises = extract_exercises_from_text(text)
            print(f"[INFO] Extracted {len(exercises)} exercises from {txt_file.name}")
            return exercises

    print("[ERROR] No exercise source file found. Exiting.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Already-completed tracking (so we can resume safely)
# ---------------------------------------------------------------------------
def load_completed() -> set[str]:
    """Return set of already-solved exercise keys like 'Exercise 3.1'."""
    completed = set()
    if not OUTPUT_PATH.exists():
        return completed
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r'^## (Exercise|Problem)\s+3\.\d+', line)
            if m:
                completed.add(line.strip().lstrip("# ").strip())
    return completed

# ---------------------------------------------------------------------------
# ZhipuAI call with retry on rate-limit errors
# ---------------------------------------------------------------------------
def call_zhipu(prompt: str) -> str:
    """Call ZhipuAI chat completion with retry logic for 429 / 1302 errors."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a world-class Quantum Computing professor and an expert academic LaTeX typesetter. "
                            "Your task is to solve exercises/problems from Chapter 3 of Nielsen & Chuang ('Quantum Computation and Quantum Information') "
                            "based on raw, dirty PDF text, and format the output perfectly.\n\n"
                            "CRITICAL INSTRUCTIONS:\n"
                            "1. ACCURACY FIRST: You must solve the problem mathematically and logically correctly. Provide rigorous, step-by-step deductions. Do not hallucinate theorems.\n"
                            "2. CLEAN AND RECONSTRUCT: The input text is from a PDF. You must ignore artifacts like '===== PAGE X =====' and fix broken lines. "
                            "MOST IMPORTANTLY, the PDF extraction dropped inline images of logic gates (e.g., NOT, AND, OR, XOR, NAND, CNOT) and some math symbols. "
                            "You must infer and reconstruct these missing gates and symbols based on the quantum/classical computing context.\n"
                            "3. STRICT ENGLISH & LATEX: The entire output MUST be in formal academic ENGLISH. Use strict LaTeX for all mathematical expressions ($...$ for inline, $$...$$ for block equations).\n"
                            "4. EXACT FORMATTING: You must strictly follow the Markdown structure below (matching the Chapter 2 style):\n\n"
                            "### [Type] [Number] [(Optional Title from text)]\n\n"
                            "**Problem:**\n"
                            "[The cleaned, fully reconstructed English problem statement.]\n\n"
                            "**Solution:**\n"
                            "[Your rigorous, correct step-by-step solution.]\n"
                            "[Append $\\square$ at the end if it is a mathematical proof.]\n\n"
                            "> **Significance:**\n"
                            "> [A brief summary explaining the contextual significance of this problem in computer science or computation theory.]\n\n"
                            "Do not output any conversational filler. Return ONLY the formatted Markdown."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Please process this extracted raw text, reconstruct the missing elements, and generate the formatted solution:\n\n{prompt}"
                    }
                ],
                temperature=0.3,
                max_tokens=4096,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            err_code = getattr(e, "status_code", None) or getattr(e, "code", None)
            err_str = str(e)
            # Check for rate-limit: HTTP 429 or zhipuai error code 1302
            is_rate_limit = (
                err_code in (429, 1302)
                or "429" in err_str
                or "1302" in err_str
                or "rate" in err_str.lower()
                or "throttl" in err_str.lower()
            )
            if is_rate_limit and attempt < MAX_RETRIES:
                wait = RETRY_DELAY * attempt  # exponential-ish backoff
                print(f"  [RATE LIMIT] {e} — retry {attempt}/{MAX_RETRIES} in {wait}s")
                time.sleep(wait)
                continue
            # Non-rate-limit error or exhausted retries
            print(f"  [API ERROR] {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
                continue
            return f"**API Call Failed**: {e}"

# ---------------------------------------------------------------------------
# Build the prompt for each exercise
# ---------------------------------------------------------------------------
def build_prompt(exercise: dict) -> str:
    ctx = exercise.get("context", "")
    text = exercise.get("text", "")
    parts = []
    if ctx:
        parts.append(f"[Context Reference]\n{ctx}\n")
    parts.append(f"[Raw Exercise Text]\n{text}")
    return "\n".join(parts)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    exercises = load_exercises()
    completed = load_completed()
    total = len(exercises)
    done_count = len(completed)

    print(f"[INFO] Total exercises: {total}  |  Already completed: {done_count}")
    print(f"[INFO] Output file: {OUTPUT_PATH}")
    print()

    # Write header only if file doesn't exist yet
    if not OUTPUT_PATH.exists():
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write("# Nielsen & Chuang — Chapter 3 Solutions\n\n")
            f.write("> Auto-generated solutions for exercises and problems from Chapter 3 "
                     "(Introduction to Computer Science).\n\n")
            f.write("---\n\n")

    for idx, ex in enumerate(exercises, 1):
        # Build a unique key, e.g. "Exercise 3.1" or "Problem 3.4"
        key = f"{ex['type']} 3.{ex['number']}"
        heading = f"## {key}"

        if key in completed:
            print(f"[{idx}/{total}] {key} — already done, skipping")
            continue

        print(f"[{idx}/{total}] Solving {key} ...", end=" ", flush=True)
        prompt = build_prompt(ex)
        solution = call_zhipu(prompt)

        # Append to file
        with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
            f.write(f"{solution}\n\n")
            f.write("---\n\n")

        print("✓")
        completed.add(key)

        # Mandatory inter-call delay
        time.sleep(INTER_CALL_DELAY)

    print(f"\n[DONE] All {total} exercises processed. Output → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

"""
Extract all exercises and problems from Nielsen & Chuang Chapter 3 PDF.
Outputs structured data for each exercise/problem including:
- Number and title
- Full text of the exercise
- Context (surrounding text before the exercise)
"""

import pymupdf
import re
import json

PDF_PATH = "/Users/wumingzhe/Downloads/ShanghaiJiaoTongUniversity/学习资料/AAA本学期课程AAA/Agent_based_Learning/quantum computation/chapter03/textbook_chapter3.pdf"

doc = pymupdf.open(PDF_PATH)

# Extract all text with page markers
full_text = ""
for i, page in enumerate(doc):
    text = page.get_text()
    full_text += f"\n===== PAGE {i+1} =====\n{text}"

# Save full extracted text for reference
with open("/Users/wumingzhe/Downloads/ShanghaiJiaoTongUniversity/学习资料/AAA本学期课程AAA/Agent_based_Learning/quantum computation/chapter03/full_extracted.txt", "w") as f:
    f.write(full_text)

print(f"Total pages: {doc.page_count}")
print(f"Total characters: {len(full_text)}")

# Find all exercise and problem markers
# Pattern: "Exercise 3.X:" or "Problem 3.X:"
exercise_pattern = r'(Exercise 3\.\d+:.*?)(?=\nExercise 3\.|Problem 3\.|===== PAGE|\Z)'
problem_pattern = r'(Problem 3\.\d+:.*?)(?=\nProblem 3\.|===== PAGE|\Z)'

# More precise: find positions of all exercises and problems
markers = []
for m in re.finditer(r'(Exercise|Problem) 3\.(\d+):', full_text):
    markers.append({
        'type': m.group(1),
        'number': int(m.group(2)),
        'start': m.start(),
        'full_match': m.group(0)
    })

print(f"\nFound {len(markers)} exercises/problems:")
for m in markers:
    print(f"  {m['type']} 3.{m['number']} at position {m['start']}")

# Extract each exercise/problem with context
exercises = []
for i, marker in enumerate(markers):
    # Find end position (start of next marker, or end of text)
    if i + 1 < len(markers):
        end_pos = markers[i+1]['start']
    else:
        end_pos = len(full_text)
    
    # Extract context (500 chars before the exercise)
    context_start = max(0, marker['start'] - 800)
    context = full_text[context_start:marker['start']].strip()
    
    # Extract full exercise text
    exercise_text = full_text[marker['start']:end_pos].strip()
    
    exercises.append({
        'type': marker['type'],
        'number': marker['number'],
        'title': marker['full_match'],
        'text': exercise_text,
        'context': context
    })

# Save structured data
output_path = "/Users/wumingzhe/Downloads/ShanghaiJiaoTongUniversity/学习资料/AAA本学期课程AAA/Agent_based_Learning/quantum computation/chapter03/exercises_raw.json"
with open(output_path, "w") as f:
    json.dump(exercises, f, indent=2, ensure_ascii=False)

print(f"\nSaved {len(exercises)} exercises to {output_path}")

# Print summary
for ex in exercises:
    print(f"\n{'='*60}")
    print(f"{ex['type']} 3.{ex['number']}")
    print(f"{'='*60}")
    # Print first 300 chars of text
    print(ex['text'][:300])
    print("...")

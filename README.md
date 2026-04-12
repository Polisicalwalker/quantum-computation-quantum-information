# Nielsen & Chuang — Quantum Computation and Quantum Information

习题解答汇总，按章节分目录存放。

## 目录结构

```
.
├── README.md
├── README_en.md
├── chapter02/              # Chapter 2: Introduction to Quantum Mechanics
│   ├── textbook_chap2.pdf              # 原书章节 PDF
│   ├── solutions_chap2_A4.pdf          # 习题解答 PDF (A4 版)
│   ├── solutions_chap2_us_letter.pdf   # 习题解答 PDF (US Letter 版)
│   └── solutions.md                    # 习题解答 (Markdown)
├── chapter03/              # Chapter 3: (待添加)
└── trash/                  # 过程性/中间文件
    └── chapter2_process_files/
```

## 命名规范

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| 原书章节 | `textbook_chapXX.pdf` | `chapter02/textbook_chap2.pdf` |
| 习题解答 Markdown | `solutions.md` | `chapter02/solutions.md` |
| 习题解答 PDF (A4) | `solutions_chapXX_A4.pdf` | `chapter02/solutions_chap2_A4.pdf` |
| 习题解答 PDF (US Letter) | `solutions_chapXX_us_letter.pdf` | `chapter02/solutions_chap2_us_letter.pdf` |

## 说明

- `trash/` 存放 agent 生成过程中的中间文件（提取文本、原始数据等），不删除但移出主目录
- 新增章节时，在根目录创建 `chapterXX/` 文件夹，按相同规范命名

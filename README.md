# 🏆 2025 Wichita Regional AI Prompt Competition - Challenge #4

**Competition:** [2025 Wichita Regional AI Prompt Championship](https://www.aipromptchamp.com)
**Challenge:** Punchcard Decoding Race
**Date:** October 2025

This repository contains the solution for Challenge #4 of the 2025 Wichita Regional AI Prompt Competition - a time-based punchcard decoding challenge.

---

## 🎯 The Challenge

**Challenge #4: Punchcard Decoder**

**Task:** You have been given a handful of punchcards that need to be uploaded into the system. It's a race against time.

Punch cards can be found here:
https://drive.google.com/drive/folders/1u00rg3yZLsqcCRmwzDQGzWbRG47vdYGD?usp=sharing

**Core Required Features:**
- Solve the riddle as fast as possible

---

## 📁 Repository Contents

### Data Directory (`/data/`)
Contains 27 encoded text files with various unusual filenames:
- `1238TERs.txt`, `AHS3jfd.txt`, `ASDUwe8wr.txt`, `sd92j342.txt`, etc.
- Each file contains encoded data that needs to be decoded to reveal the hidden message

### Decoder Scripts

- **`decode_punchcards.py`** - Primary decoder for IBM punchcard format
- **`decode_alternative.py`** - Alternative decoding strategies
- **`decode_utf8.py`** - UTF-8 based decoding approach
- **`analyze_filenames.py`** - Analyzes file naming patterns for clues

### Prompts Directory (`/prompts/`)

- **`punchcard_decoder.md`** - Master prompt and decoding strategies

---

## 🔍 Methodology

The challenge required:

1. **Pattern Recognition** - Identifying the encoding format (IBM punchcard format)
2. **Rapid Analysis** - Quickly analyzing multiple files to find patterns
3. **Decoding Strategy** - Implementing multiple decoding approaches in parallel
4. **Time Pressure** - Racing against the clock to solve the riddle

---

## 🚀 Quick Start

### Running the Decoders

```bash
# Primary punchcard decoder
python decode_punchcards.py

# Alternative decoding methods
python decode_alternative.py

# UTF-8 decoding approach
python decode_utf8.py

# Analyze filename patterns
python analyze_filenames.py
```

---

## 📝 Competition Context

This challenge tested:
- **Speed** - Quick analysis and implementation under time pressure
- **Pattern Recognition** - Identifying obscure encoding formats
- **Problem Solving** - Trying multiple approaches when first attempts fail
- **AI Collaboration** - Effective prompting to guide AI through the decoding process

---

**Competition Date:** October 2025
**Repository Created:** October 2025

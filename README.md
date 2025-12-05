# 🧠 AIMO Project – Local Mathematical Olympiad Evaluation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **A complete environment for loading, solving, submitting, and scoring AI-generated mathematical reasoning tasks.**

---

## 📖 Overview

This repository simulates an **AI Mathematical Olympiad (AIMO)** competition environment.  
It provides a local evaluation sandbox identical to official AI reasoning competitions.

With this framework, you can:

- 📥 **Load** Olympiad-style math problems  
- 🧠 **Develop & run** custom solvers  
- 📝 **Submit** answers programmatically  
- 📊 **Score** predictions using competition rules  
- 📄 **Generate** automatic `submission.csv` submissions  

---

# 📂 AIMO Project – Full File-by-File Documentation

This document explains **every folder and every file** inside the AIMO Project repository, based entirely on your provided directory structure.  
Nothing is omitted. This is the **complete and official technical breakdown** suitable for a GitHub README.

---

# 🏗️ Repository Structure (Explained in Detail)

Below is the full project layout you uploaded:

```
AIMO_Project/
│
├── aimo_api/
│   ├── __pycache__/
│   ├── client.py
│   ├── loader.py
│   ├── ordering.py
│   ├── scorer.py
│
├── api/
│   ├── __init__.py
│
├── baselines/
│   ├── __pycache__/
│   ├── simple_baseline.py
│   ├── solver.py
│
├── evaluator/
│   ├── __init__.py
│   ├── loader.py
│   ├── scoring.py
│
├── problems/
│   ├── problems.json
│   ├── sample_problems.json
│
├── solver/
│   ├── __init__.py
│   ├── model_solver.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── run1_submission.csv
├── submission.csv
├── submission_template.py
├── test_runner.py
├── LICENSE
├── README.md
```

---

# 🔵 1. Folder: `aimo_api/`

A legacy or alternative version of the API/evaluator system. It contains an older pipeline for loading problems, ordering them, running scoring, and interacting with a client. Likely preserved for backward compatibility.

## 📄 `aimo_api/client.py`
- Earlier version of the main API client.
- Handles:
  - Loading problems
  - Serving problems sequentially
  - Accepting solver submissions
  - Tracking state

## 📄 `aimo_api/loader.py`
- Loads datasets (JSON files) used by the competition.
- Validates entries and returns structured problem lists.

## 📄 `aimo_api/ordering.py`
- Controls the order in which problems are delivered.
- Can include:
  - Shuffling
  - Sorting
  - Curriculum ordering
  - Seeding for reproducibility

## 📄 `aimo_api/scorer.py`
- Legacy scoring system.
- Compares predictions to answers.
- Computes score breakdowns.

## 📁 `aimo_api/__pycache__/`
- Auto-generated Python bytecode.
- Not important; ignored by Git.

---

# 🔵 2. Folder: `api/`

This is the **active, modern API layer** used by solvers.

## 📄 `api/__init__.py`
- Initializes the API package.
- Enables imports like:

```python
from api import client
```

---

# 🟢 3. Folder: `baselines/`

Contains **baseline solver examples** used for testing and demonstrating the environment.

## 📄 `baselines/simple_baseline.py`
- A very simple solver for demonstration.
- Responsibilities:
  - Fetch problem using `AIMOClient`
  - Produce trivial or default answers
  - Submit those answers back to evaluator

## 📄 `baselines/solver.py`
- Base solver class or template.
- Provides reusable logic for other solvers.
- Sometimes contains:
  - Parsing utilities
  - Generic solve() methods
  - A structure to extend custom solvers

## 📁 `baselines/__pycache__/`
- Auto-generated Python cache files.

---

# 🟠 4. Folder: `evaluator/`

This is the **official scoring and data-loading engine** for the entire system.

## 📄 `evaluator/__init__.py`
- Initializes evaluator package.

## 📄 `evaluator/loader.py`
- Loads/validates problem JSON files.
- Ensures each problem has:
  - `id`
  - `latex`
  - `answer`
- Checks uniqueness of IDs.

## 📄 `evaluator/scoring.py`
- Main scoring script.
- Compares solver predictions vs. ground truth.
- Computes:
  - Total solved
  - Correct count
  - Accuracy percentage
- Generates:
  - `submission.csv`
  - Detailed scoring breakdown

---

# 🟣 5. Folder: `problems/`

Contains datasets the solver will use.

## 📄 `problems/problems.json`
- A full or alternative dataset of problems.

## 📄 `problems/sample_problems.json`
- Default dataset loaded by `test_runner.py`.
- Example structure:

```json
{
  "id": "p1",
  "latex": "Compute 2 + 2.",
  "answer": 4
}
```

---

# 🟤 6. Folder: `solver/`

This contains **your actual solver implementation** (not baseline).

## 📄 `solver/__init__.py`
- Package initializer.

## 📄 `solver/model_solver.py`
- Your custom solver.
- Can implement:
  - LLM-based reasoning
  - Rule-based math solving
  - Heuristic systems
- Integrated with `AIMOClient`.

This is the file YOU modify to create an intelligent agent.

---

# ⚫ 7. Project Root Files

## 📄 `.gitignore`
Specifies which files Git should ignore, e.g.:
- `__pycache__/`
- `.env`
- `*.pyc`
- `submission.csv`

## 📄 `README.md`
Your project documentation.

## 📄 `requirements.txt`
Lists dependencies. Installed via:

```bash
pip install -r requirements.txt
```

## 📄 `run1_submission.csv`
A **sample submission** produced by a past run.

## 📄 `submission.csv`
The **latest generated submission**, created by scoring after running:

```bash
python test_runner.py
```

## 📄 `submission_template.py`
Template file for producing competition-style submissions.
Contains:
- Example solve loop
- Submission formatting rules

## 📄 `test_runner.py`
🔥 The **central orchestrator** for the entire system.

**Responsibilities:**
1. Load problems from `/problems/sample_problems.json`
2. Create an AIMOClient instance
3. Run a solver (baseline or your custom solver)
4. Collect predictions
5. Score using evaluator/scoring.py
6. Save results to `submission.csv`
7. Print scoring summary

Used like:

```bash
python test_runner.py
```

## 📄 `LICENSE`
License file (MIT).

## 📄 `README.md` (duplicate)
A second README, probably accidental. Should remove one to avoid confusion.

---

# ✅ Summary

This document represents the **entire technical breakdown of every file** in your repository.

Use it directly as:
✔ Documentation  
✔ Contributor onboarding  
✔ GitHub README section  
✔ Internal team reference  

---


## ⭐ Acknowledgements

Inspired by academic AI reasoning benchmarks including:

- AI Mathematical Olympiads  
- MATH dataset  
- GSM8K reasoning tasks  

---

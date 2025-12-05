# 🧠 AIMO Project – Local Mathematical Olympiad Evaluation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **A complete environment for loading, solving, submitting, and scoring AI-generated mathematical reasoning tasks.**

---

## 📖 Overview

This repository simulates an **AI Mathematical Olympiad (AIMO)** competition environment. It provides a local evaluation sandbox identical in structure to official competitions, allowing you to:

- 📥 **Load** Olympiad-style math problems.
- 🏃 **Run** a baseline or custom solver.
- 📝 **Submit** answers to an internal evaluator.
- 📊 **Score** your model’s performance exactly like a real AI competition.
- 📄 **Generate** an automatic `submission.csv`.

---

## 📁 Repository Structure

The project is organized to separate the evaluation logic from the problem datasets and solver implementations.

```text
AIMO_Project/
│
├── README.md              # Project Documentation
├── requirements.txt       # Python Dependencies
│
├── api/                   # Simulation of the Competition API
│   ├── __init__.py
│   └── client.py          # The AIMOClient class
│
├── evaluator/             # Internal Scoring Logic
│   ├── __init__.py
│   ├── scoring.py         # Scoring rules and CSV generation
│   └── loader.py          # Problem dataset loader
│
├── problems/              # Data Storage
│   └── sample_problems.json
│
├── baselines/             # Example Solvers
│   └── simple_baseline.py
│
├── utils/                 # (Optional) Helper functions
│   └── helpers.py
│
├── submission.csv         # Output file (Generated after running)
└── test_runner.py         # Main execution script

## 🔍 Component Details

### 1. The API (`api/`)
A simulated interface that mirrors how official AIMO competition servers interact with models.

| Function | Description |
| :--- | :--- |
| `get_next()` | Fetches the next problem object from the queue. |
| `submit(id, answer)` | Stores the prediction for the specific problem ID. |
| `reset()` | Clears the current state (useful for restarting runs). |

### 2. The Evaluator (`evaluator/`)
- **`loader.py`**: Loads problems from JSON, ensuring fields like `id`, `latex`, and `answer` exist.
- **`scoring.py`**: Compares predictions with ground truth, calculates the final score, and writes the results to `submission.csv`.

### 3. Problem Format (`problems/`)
Problems are stored in `sample_problems.json` following this strict schema:

```json
{
  "id": "p4",
  "latex": "What is 10 + 10?",
  "answer": 20
}

## 🛠 Installation & Setup

### Prerequisites
* Python 3.8 or higher

### Step 1: Verify Python
```powershell
python --version

### Step 2: Clone & Navigate
Navigate to the project directory (update the path to match your local machine).

```powershell
cd C:\Users\Vittal\OneDrive\Desktop\Math_Olympiad\open-math-reasoning-suite\AIMO_Project

### Step 2: Dependencies
pip install -r requirements.txt

## ▶️ Usage Guide

### Running the Evaluation
To run the full simulation—which loads problems, runs the solver, and grades the results—execute the test runner:

```powershell
python test_runner.py

**Expected Output:**
1.  Console log showing progress.
2.  Final Score summary.
3.  Generation of `submission.csv` in the root folder.

### Adding Custom Problems
You can extend the dataset by editing `problems/sample_problems.json`.

**Example:**
```json
[
  ...
  {
    "id": "p7",
    "latex": "Find the value of 3^3.",
    "answer": 27
  }
]

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

## 📁 Repository Structure

The project is structured to cleanly separate the evaluation logic, datasets, and solver implementations.

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
```

---

## 🔍 Component Details

### 🔹 1. API Layer (`api/`)

A simulated interface that mirrors how real competition servers interact with models.

| Function | Description |
|---------|-------------|
| `get_next()` | Returns the next unsolved problem from the queue |
| `submit(id, answer)` | Records the solver's prediction |
| `reset()` | Clears internal state for a fresh run |

---

### 🔹 2. Evaluator (`evaluator/`)

- **`loader.py`**  
  Loads JSON problems and ensures required fields:  
  - `id`  
  - `latex`  
  - `answer`

- **`scoring.py`**  
  - Compares model predictions with ground truth  
  - Computes a final score  
  - Generates `submission.csv`  
  - Prints a detailed scoring breakdown  

---

### 🔹 3. Problem Format (`problems/`)

All problems follow a strict schema inside `sample_problems.json`:

```json
{
  "id": "p4",
  "latex": "What is 10 + 10?",
  "answer": 20
}
```

---

## 🛠 Installation & Setup

### ✅ Prerequisites  
- Python **3.8+**

---

### ▶️ Step 1: Verify Python Installation

```powershell
python --version
```

---

### ▶️ Step 2: Navigate to the Project Directory

> Update the path according to your machine.

```powershell
cd C:\Users\Vittal\OneDrive\Desktop\Math_Olympiad\open-math-reasoning-suite\AIMO_Project
```

---

### ▶️ Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Usage Guide

### 🔥 Running the Evaluation

```powershell
python test_runner.py
```

### ✔ Expected Output:

- A console log showing progress  
- Final score summary  
- A generated **`submission.csv`** in the project folder  

---

## ➕ Adding Custom Problems

Open:

```
problems/sample_problems.json
```

### Example Problem Entry:

```json
{
  "id": "p7",
  "latex": "Find the value of 3^3.",
  "answer": 27
}
```

Be sure to maintain **valid JSON formatting**.

---

## 🤖 Adding Custom Solvers

Create your own solver in:

```
baselines/my_solver.py
```

Example template:

```python
from api.client import AIMOClient

def run():
    client = AIMOClient()
    problem = client.get_next()

    while problem:
        # Replace with your model's logic
        answer = 0
        client.submit(problem["id"], answer)
        problem = client.get_next()
```

Then modify `test_runner.py` to call your solver instead of the baseline.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

Inspired by academic AI reasoning benchmarks including:

- AI Mathematical Olympiads  
- MATH dataset  
- GSM8K reasoning tasks  

---

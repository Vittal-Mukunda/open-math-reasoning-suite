# AIMO Project

## Overview
This is a local development environment for an AI Mathematical Olympiad evaluation system. It provides a framework for loading mathematical problems, running baseline models, submitting answers, and scoring the results.

## Folder Structure
```
AIMO_Project/
    README.md
    requirements.txt

    api/
        __init__.py
        client.py           # Client to interact with the evaluation environment

    evaluator/
        __init__.py
        scoring.py          # Scoring logic
        loader.py           # Problem loader

    problems/
        sample_problems.json # Sample dataset

    baselines/
        simple_baseline.py  # Example primitive solver

    test_runner.py          # Main script to run the evaluation
```

## How to Install the Environment
1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Test Runner
Run the main test script from the root of the project (or ensure the python path is correct):

```bash
cd AIMO_Project
python3 test_runner.py
```

This will:
- Load the sample problems.
- Run the simple baseline solver.
- Generate a `submission.csv` file.
- Print the score and a detailed breakdown.

## How to Add New Problems
Edit `problems/sample_problems.json` and add entries in the following format:
```json
{
  "id": "p4",
  "latex": "What is 10 + 10?",
  "answer": 20
}
```

## How to Build Models / Baselines
Create a new script or modify `baselines/simple_baseline.py`. Your solver should:
1. Import `AIMOClient` from `api.client`.
2. Iterate through problems using `client.get_next()`.
3. Compute the answer.
4. Submit the answer using `client.submit(problem_id, answer)`.

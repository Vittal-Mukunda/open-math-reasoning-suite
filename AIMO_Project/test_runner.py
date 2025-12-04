import sys
import os

# Add the current directory to sys.path so we can import from the project modules
sys.path.append(os.getcwd())

from api.client import AIMOClient
from evaluator import loader, scoring
from baselines import simple_baseline

def main():
    # Load problems
    # The loader expects the path to be relative to where it is run, or absolute.
    # Since we run from AIMO_Project root usually, problems/sample_problems.json is correct.
    try:
        problems = loader.load_problems("problems/sample_problems.json")
    except FileNotFoundError:
        # Fallback if running from parent directory
         problems = loader.load_problems("AIMO_Project/problems/sample_problems.json")

    # Create Client
    client = AIMOClient(problems)

    # Run Baseline
    # The baseline expects the client and drives the loop
    simple_baseline.solve(client)

    # Save output
    client.save("submission.csv")
    print("Saved submission.csv")

    # Score
    # Prepare answers dict
    answers = {p["id"]: p["answer"] for p in problems}

    total_score, breakdown = scoring.score(client.predictions, answers)

    # Print results
    print(f"Score: {total_score}/{len(problems)}")
    print(f"Detailed breakdown: {breakdown}")

if __name__ == "__main__":
    main()

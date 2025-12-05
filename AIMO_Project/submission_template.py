# ----------------------------------------------------------
# IMPORT HYBRID SOLVER (DeepSeek-R1-Distill-7B)
# ----------------------------------------------------------

from baselines.solver import solve_with_default, get_default_solver

def solve_problem_lm(latex: str) -> int:
    """
    Wrapper for your hybrid solver.
    Loads the model once, then solves each problem.
    """
    return solve_with_default(latex)


# ----------------------------------------------------------
# AIMO API IMPORTS
# ----------------------------------------------------------

from aimo_api.loader import load_problems, build_answer_map
from aimo_api.client import AIMOClient
from aimo_api.scorer import score_single_run, score_two_runs


# ----------------------------------------------------------
# RUN ONE PASS THROUGH ALL PROBLEMS
# ----------------------------------------------------------

def run_once(problems, mode, seed, solver):
    """
    Runs a single evaluation pass using the specified solver:
    - mode="public"  → random seeded order
    - mode="private" → deterministic sorted order
    """
    client = AIMOClient(problems=problems, mode=mode, seed=seed)

    while True:
        item = client.get_next()
        if item is None:
            break

        pid = item["id"]
        latex = item["latex"]

        # Solve using LLM-based solver
        answer = solver(latex)

        client.submit(pid, answer)

    return client.get_prediction_dict()


# ----------------------------------------------------------
# MAIN PIPELINE
# ----------------------------------------------------------

def main():

    print("Loading problems + answers...")
    problems = load_problems("problems/problems.json")
    answers = build_answer_map(problems)

    print("\nLoading DeepSeek Hybrid Solver (first load only)...")
    _ = get_default_solver()   # Load model once for speed

    # -------------------------
    # RUN 1 — Public
    # -------------------------
    seed_run1 = 12345
    print(f"\nRunning run 1 (public, seed={seed_run1})...")
    run1 = run_once(
        problems=problems,
        mode="public",
        seed=seed_run1,
        solver=solve_problem_lm
    )

    # -------------------------
    # RUN 2 — Private
    # -------------------------
    seed_run2 = 54321
    print("\nRunning run 2 (private)...")
    run2 = run_once(
        problems=problems,
        mode="private",
        seed=seed_run2,
        solver=solve_problem_lm
    )

    # -------------------------
    # SCORING
    # -------------------------
    print("\nScoring run 1...")
    single1, _ = score_single_run(run1, answers)
    print(f"Run 1 score: {single1}")

    print("\nScoring run 2...")
    single2, _ = score_single_run(run2, answers)
    print(f"Run 2 score: {single2}")

    print("\nComputing official combined score...")
    combined, _ = score_two_runs(run1, run2, answers)
    print(f"Combined score: {combined}")

    # -------------------------
    # SAVE SUBMISSION
    # -------------------------
    print("\nSaving submission.csv...")

    with open("submission.csv", "w", encoding="utf-8") as f:
        f.write("problem_id,answer\n")
        for pid, ans in run1.items():
            f.write(f"{pid},{ans}\n")

    print("submission.csv saved successfully!")


# ----------------------------------------------------------
# RUN SCRIPT
# ----------------------------------------------------------

if __name__ == "__main__":
    main()

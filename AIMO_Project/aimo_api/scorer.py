# ============================
# AIMO Scoring Functions
# ============================

def score_single_run(predictions, answers):
    """
    Correct = 1 point
    Incorrect = 0 points
    """
    score = 0
    breakdown = {}

    for pid, true_answer in answers.items():
        pred_answer = predictions.get(pid)

        if pred_answer == true_answer:
            score += 1
            breakdown[pid] = "Correct"
        else:
            breakdown[pid] = "Incorrect"

    return score, breakdown


def score_two_runs(run1, run2, answers):
    """
    AIMO official scoring:
    - If both runs correct  -> 1 point
    - If one correct        -> 0.5 points
    - If none correct       -> 0 points
    """
    total = 0
    breakdown = {}

    for pid, true_answer in answers.items():
        p1 = run1.get(pid)
        p2 = run2.get(pid)

        if p1 == true_answer and p2 == true_answer:
            score = 1
        elif p1 == true_answer or p2 == true_answer:
            score = 0.5
        else:
            score = 0

        breakdown[pid] = score
        total += score

    return total, breakdown

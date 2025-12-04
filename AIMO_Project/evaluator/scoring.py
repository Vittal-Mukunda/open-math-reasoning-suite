def score(predictions, answers):
    """
    predictions = list of (problem_id, answer)
    answers = dict mapping "p1": correct_value

    Scoring rules:
    1 point if the submission matches the correct answer.
    0 points otherwise.

    Returns total score + a per-problem breakdown.
    """
    total_score = 0
    breakdown = {}

    # Convert predictions to a dict for easier lookup, or iterate
    # The requirement says predictions is a list of (problem_id, answer)

    # Check each prediction
    for pid, predicted_val in predictions:
        correct_val = answers.get(pid)

        # Simple equality check. In a real system, might need float tolerance or string normalization.
        # Assuming sample problems have integer answers.
        # We cast both to string to be safe or float if numeric.
        # The sample baseline returns integers. Sample answers are integers.
        # Let's try direct comparison first, if fails try string comparison.

        is_correct = False
        if correct_val is not None:
            if predicted_val == correct_val:
                is_correct = True
            elif str(predicted_val).strip() == str(correct_val).strip():
                is_correct = True

        if is_correct:
            total_score += 1
            breakdown[pid] = "Correct"
        else:
            breakdown[pid] = "Incorrect"

    return total_score, breakdown

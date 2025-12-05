from aimo_api.loader import load_problems
from aimo_api.ordering import deterministic_order, seeded_random_order

class AIMOClient:
    def __init__(self, problems=None, problems_file="problems/problems.json",
                 mode="public", seed=1234):
        """
        mode = "public"  -> shuffled order (simulates Kaggle public leaderboard)
        mode = "private" -> deterministic order (simulates final evaluation)
        """

        # Load problems if none were provided
        if problems is None:
            problems = load_problems(problems_file)

        # Apply ordering rules
        if mode == "public":
            self.problems = seeded_random_order(problems, seed)
        else:
            self.problems = deterministic_order(problems)

        self.index = 0
        self.predictions = []

    def get_next(self):
        """Return next problem as {'id':..., 'latex':...} or None."""
        if self.index >= len(self.problems):
            return None

        p = self.problems[self.index]
        self.index += 1
        return {"id": p["id"], "latex": p["latex"]}

    def submit(self, problem_id, answer):
        """Store prediction."""
        self.predictions.append((problem_id, int(answer)))

    def get_prediction_dict(self):
        """Return predictions as a dictionary: {problem_id: answer}."""
        return {pid: ans for pid, ans in self.predictions}

import csv

class AIMOClient:
    def __init__(self, problems):
        """
        Stores the list of problems, resets pointer, creates predictions list.
        """
        self.problems = problems
        self.pointer = 0
        self.predictions = []

    def get_next(self):
        """
        Returns next problem as a dict with fields { "id": ..., "latex": ... }, or None if done.
        """
        if self.pointer >= len(self.problems):
            return None

        problem = self.problems[self.pointer]
        self.pointer += 1

        # Return only id and latex to simulate the environment
        return {
            "id": problem["id"],
            "latex": problem["latex"]
        }

    def submit(self, problem_id, answer):
        """
        Adds (problem_id, answer) to internal list.
        """
        self.predictions.append((problem_id, answer))

    def save(self, filename="submission.csv"):
        """
        Writes CSV:
        problem_id,answer
        p1,123
        p2,456

        Must contain no hidden BOM characters.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['problem_id', 'answer'])
            for pid, ans in self.predictions:
                writer.writerow([pid, ans])

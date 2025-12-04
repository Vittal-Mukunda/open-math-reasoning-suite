import json
import os

def load_problems(filename="problems/sample_problems.json"):
    """
    Loads problems from problems/sample_problems.json.
    Returns them as a Python list.
    Ensures each problem has "id" and "latex".
    """
    # Adjust path if running from different directories
    # Assuming execution from AIMO_Project root or where test_runner is
    if not os.path.exists(filename):
         # Try looking relative to this file
         base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
         potential_path = os.path.join(base_dir, filename)
         if os.path.exists(potential_path):
             filename = potential_path
         else:
             # Fallback if just the filename is given and we are in the root
             pass

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Validate structure
    for problem in data:
        if "id" not in problem or "latex" not in problem:
            raise ValueError(f"Problem missing id or latex: {problem}")

    return data

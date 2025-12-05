import json
from pathlib import Path
from typing import List, Dict

def load_problems(path="problems/problems.json") -> List[Dict]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Problems file not found: {p.resolve()}")
    with p.open("r", encoding="utf-8") as f:
        problems = json.load(f)
    return problems

def build_answer_map(problems: List[Dict]) -> Dict[str, int]:
    return {p["id"]: int(p["answer"]) for p in problems}

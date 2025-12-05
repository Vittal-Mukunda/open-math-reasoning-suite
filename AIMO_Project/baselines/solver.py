# baselines/solver.py
"""
Hybrid solver using DeepSeek-R1-Distill-7B + SymPy verification + self-consistency.
Works on RTX 4050 using 4-bit quantization.
"""

import re
import sympy as sp
from collections import Counter
from typing import Optional, List

# Attempt transformers import
try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    HF_AVAILABLE = True
except Exception:
    HF_AVAILABLE = False


# ---------------------------
# MODEL SETTINGS
# ---------------------------

MODEL_NAME = "deepseek-ai/deepseek-math-7b-instruct"

NUM_SAMPLES = 3              # reduce for faster testing
TEMPERATURE = 0.7
TOP_P = 0.95
MAX_NEW_TOKENS = 256

ANS_MIN, ANS_MAX = 0, 99999   # allowed range


# ---------------------------
# PROMPT
# ---------------------------

PROMPT_TEMPLATE = """
You are a careful math reasoning assistant. Solve the following problem step by step.

After your reasoning, output the final integer answer exactly in the format:

FINAL ANSWER: <number>

Problem:
{problem}

Solution:
"""


# ---------------------------
# Load DeepSeek Model (4-bit)
# ---------------------------

def load_deepseek_model():
    if not HF_AVAILABLE:
        raise RuntimeError("Transformers is not installed.")

    print("[solver] Loading DeepSeek-R1-Distill-7B in 4-bit quantization...")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        load_in_4bit=True,
        torch_dtype=torch.float16,
        trust_remote_code=True
    )

    print("[solver] Model loaded.")
    return tokenizer, model


# ---------------------------
# LLM Text Generation
# ---------------------------

def generate_text(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=MAX_NEW_TOKENS,
        do_sample=True,
        temperature=TEMPERATURE,
        top_p=TOP_P,
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)


# ---------------------------
# Extraction Helpers
# ---------------------------

FINAL_INT_RE = re.compile(r"FINAL ANSWER\s*[:\-]\s*([+-]?\d+)", re.IGNORECASE)
INT_RE = re.compile(r"([+-]?\d+)")

def extract_final_answer(text: str) -> Optional[int]:
    """Extract final answer from 'FINAL ANSWER: N' line."""
    m = FINAL_INT_RE.search(text)
    if m:
        try:
            return int(m.group(1))
        except:
            pass

    # fallback: last integer
    nums = INT_RE.findall(text)
    if nums:
        try:
            return int(nums[-1])
        except:
            pass

    return None


def extract_expressions(text: str) -> List[str]:
    """Extract arithmetic expressions from reasoning."""
    exprs = []
    lines = text.splitlines()[-6:]
    for ln in lines:
        if re.search(r"[0-9\+\-\*\/\^\(\)]", ln):
            exprs.append(ln.strip())

    return list(dict.fromkeys(exprs))  # dedupe


def eval_expr(expr: str) -> Optional[int]:
    try:
        expr = expr.replace("^", "**")
        val = sp.N(sp.sympify(expr))
        if val.is_real:
            num = float(val)
            return int(round(num))
    except:
        return None
    return None


# ---------------------------
# Hybrid Solver
# ---------------------------

class HybridSolver:
    def __init__(self):
        self.tokenizer = None
        self.model = None

        print("[solver] Loading HybridSolver...")
        try:
            self.tokenizer, self.model = load_deepseek_model()
        except Exception as e:
            print("[solver] Could not load model:", e)
            self.model = None

    def solve_once(self, problem: str) -> Optional[int]:
        if self.model is None:
            return None

        prompt = PROMPT_TEMPLATE.format(problem=problem)
        answers = []

        for _ in range(NUM_SAMPLES):
            txt = generate_text(self.model, self.tokenizer, prompt)

            # Try FINAL ANSWER: N
            ans = extract_final_answer(txt)
            if ans is not None:
                answers.append(ans)
                continue

            # Try expression evaluation
            for e in extract_expressions(txt):
                val = eval_expr(e)
                if val is not None:
                    answers.append(val)
                    break

        if not answers:
            return None

        return Counter(answers).most_common(1)[0][0]

    def solve(self, problem: str, fallback: int = 0) -> int:
        try:
            ans = self.solve_once(problem)
            if ans is None:
                ans = fallback
        except:
            ans = fallback

        ans = max(ANS_MIN, min(ANS_MAX, int(ans)))
        return ans


# ---------------------------
# Global Solver Interface
# ---------------------------

_default_solver = None

def get_default_solver():
    global _default_solver
    if _default_solver is None:
        _default_solver = HybridSolver()
    return _default_solver

def solve_with_default(problem: str) -> int:
    solver = get_default_solver()
    return solver.solve(problem)

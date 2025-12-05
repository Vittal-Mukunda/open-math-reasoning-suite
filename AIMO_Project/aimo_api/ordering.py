import random

def deterministic_order(problems):
    """
    Sort problems by their ID (used in private leaderboard simulation).
    """
    return sorted(problems, key=lambda p: p["id"])

def seeded_random_order(problems, seed):
    """
    Shuffle problems deterministically using a fixed seed
    (simulates Kaggle public leaderboard behavior).
    """
    rng = random.Random(seed)
    shuffled = list(problems)
    rng.shuffle(shuffled)
    return shuffled

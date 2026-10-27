
RUBRIC = {
    "correctness": {
        "weight": 0.35,
        "description": (
            "Does the answer provide factually correct "
            "information and avoid unsupported claims?"
        ),
    },
    "relevance": {
        "weight": 0.25,
        "description": (
            "Does the answer directly address the question?"
        ),
    },
    "completeness": {
        "weight": 0.20,
        "description": (
            "Does the answer cover the important parts "
            "of the question?"
        ),
    },
    "clarity": {
        "weight": 0.10,
        "description": (
            "Is the answer clear, organized, and understandable?"
        ),
    },
    "evidence": {
        "weight": 0.10,
        "description": (
            "Does the answer support its factual claims "
            "with appropriate evidence or reasoning?"
        ),
    },
}

def calculate_weighted_score(scores: dict[str,int]) -> float:
    """
    Calculate the weighted score based on a 0-100 scale.

    Args:
        scores (dict[str, int]): A dictionary containing scores for each criterion.

    Returns:
        float: The weighted score.
    """
    if set(scores) != set(RUBRIC):
        raise ValueError("Scores must contain all rubric criteria.")

    for criterion, score in scores.items():
        if not isinstance(score, int) or not (0 <= score <= 5):
            raise ValueError(f"Score for {criterion} must be an integer between 0 and 5.")

    weighted_score = sum(
        (scores[criterion] / 5) * details["weight"] * 100
        for criterion, details in RUBRIC.items()
    )
    return round(weighted_score, 2)
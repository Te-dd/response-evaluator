import pytest

from app.rubric.evaluator import calculate_weighted_score


def test_perfect_scores():
    scores = {
        "correctness": 5,
        "relevance": 5,
        "completeness": 5,
        "clarity": 5,
        "evidence": 5,
    }
    assert calculate_weighted_score(scores) == 100.0

def test_zero_scores():
    scores = {
        "correctness": 0,
        "relevance": 0,
        "completeness": 0,
        "clarity": 0,
        "evidence": 0,
    }
    assert calculate_weighted_score(scores) == 0.0

def test_invalid_scores():
    scores = {
        "correctness": 6,
        "relevance": 4,
        "completeness": 3,
        "clarity": 5,
        "evidence": 3,
    }
    with pytest.raises(ValueError):
        calculate_weighted_score(scores)

def test_missing_criteria():
    scores = {
        "correctness": 5,
        "relevance": 4,
    }
    with pytest.raises(ValueError):
        calculate_weighted_score(scores)
import pytest

from game.scripts.difficulty import check_difficulty


def test_check_difficulty_returns_score():
    result = check_difficulty('ABC')
    assert result > 0


def test_check_difficulty_calculates_properly():
    result = check_difficulty('A')
    assert round(result, 10) == 1.1057538898


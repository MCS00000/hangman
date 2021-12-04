import pytest
import requests

from bs4 import BeautifulSoup

from game.scripts.word_hint import get_hint


def test_get_hint_missing_english_term():
    result = get_hint('NonExistingWord', 2)
    assert result is None


def test_get_hint_known_english_term():
    result = get_hint('test', 2)
    assert type(result) is str and len(result) > 1


def test_get_hint_missing_latvian_term():
    result = get_hint('NeeksistējošsVārds', 1)
    assert result is None


def test_get_hint_known_latvian_term():
    result = get_hint('tests', 1)
    assert type(result) is str and len(result) > 1
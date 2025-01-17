import pytest
from src.score_card import ScoreCard

def test_check_card():
    PINS = "12345123451234512345"
    card = ScoreCard(PINS)
    assert card

def test_get_pins():
    PINS = "12345123451234512345"
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS
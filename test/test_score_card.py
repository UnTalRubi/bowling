import pytest
from src.score_card import ScoreCard

def test_check_card():
    pins = "12345123451234512345"
    card = ScoreCard(pins)
    assert card

def test_get_pins():
    pins = "12345123451234512345"
    card = ScoreCard(pins)
    assert card.get_pins() == pins

def test_calculate_total():
    pins = "12345123451234512345"
    total = 60
    card = ScoreCard(pins)
    assert total == card.calculate_total()


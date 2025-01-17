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

def test_calculate_standard():
    pins = "12345123451234512345"   
    total = 60
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_calculate_miss():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    card = ScoreCard(pins)
    assert total == card.calculate_total()

    pins = "9-3561368153258-7181"
    total = 82
    card = ScoreCard(pins)
    assert total == card.calculate_total()
    
def test_spare():
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    card = ScoreCard(pins)
    assert total == card.calculate_total()
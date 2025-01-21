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

def test_strike():
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    card = ScoreCard(pins)
    assert total == card.calculate_total()
    
    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_two_strike():
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_three_strike():
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_one_pin_in_extra_roll():
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    card = ScoreCard(pins)
    assert total == card.calculate_total()

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_two_strikes_in_extra_rolls():
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_one_strike_in_extra_roll():
    pins = "8/549-XX5/53639/9/X"
    total = 149
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_spare_in_extra_roll():
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    card = ScoreCard(pins)
    assert total == card.calculate_total()

def test_triple_strike_before_extra_rolls():
    pins = "XXXXXXXXXXXX"
    total = 300
    card = ScoreCard(pins)
    assert total == card.calculate_total()

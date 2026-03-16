import pytest
from treys import Card
import Poker_Advie_Bot
from Poker_Advice_Bot import get_advice, card_to_str, parser


def test_get_advice():
    assert get_advice(pot_size=100, call_cost=50, equity=0.50) == "CALL"
    assert get_advice(pot_size=100, call_cost=50, equity=0.20) == "FOLD"
    assert get_advice(pot_size=1000, call_cost=10, equity=0.05) == "CALL"

def test_card_to_str():
    assert card_to_str([]) == ""
    card1 = [Card.new("Ah")]
    assert card_to_str(card1) == "Ah"
    cards = [Card.new("As"), Card.new("Kd"), Card.new("Tc")]
    assert card_to_str(cards) == "As, Kd, Tc"

def test_parser():
    project.hero_cards.clear()
    project.community_cards.clear()
    parser(["Ah", "Kd"], "preflop")
    assert len(project.hero_cards) == 2

    with pytest.raises(SystemExit):
        parser(["A", "K"], "preflop")
        
    with pytest.raises(SystemExit):
        parser(["1h", "2d"], "preflop")

    with pytest.raises(SystemExit):
        parser(["3g", "2d"], "preflop")
    
    project.community_cards.append(Card.new("2c"))
    with pytest.raises(SystemExit):
        parser(["2c"], "flop")

import pytest
from dominoes.hand import Hand, contains_value
from dominoes.domino import Domino
from dominoes.exceptions import NoSuchDominoException


def test_hand_creation():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    assert len(hand) == 2
    assert d1 in hand
    assert d2 in hand


def test_empty_hand_length():
    hand = Hand([])
    assert len(hand) == 0


def test_hand_indexing():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    assert hand[0] == d1
    assert hand[1] == d2


def test_hand_iteration():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    dominoes = list(hand)
    assert dominoes == [d1, d2]


def test_play_domino():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    index = hand.play(d1)
    assert index == 0
    assert len(hand) == 1
    assert d1 not in hand
    assert d2 in hand


def test_play_nonexistent_domino():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1])
    with pytest.raises(NoSuchDominoException):
        hand.play(d2)


def test_contains_value_true():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    assert contains_value(hand, 1) == True
    assert contains_value(hand, 2) == True
    assert contains_value(hand, 3) == True
    assert contains_value(hand, 4) == True


def test_contains_value_false():
    d1 = Domino(1, 2)
    d2 = Domino(3, 4)
    hand = Hand([d1, d2])
    assert contains_value(hand, 5) == False
    assert contains_value(hand, 0) == False


def test_contains_value_empty_hand():
    hand = Hand([])
    assert contains_value(hand, 1) == False

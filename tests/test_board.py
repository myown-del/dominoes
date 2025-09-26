import pytest
from dominoes.board import Board
from dominoes.domino import Domino
from dominoes.exceptions import EmptyBoardException, EndsMismatchException


def test_getting_domino_when_board_is_empty():
    board = Board()

    with pytest.raises(EmptyBoardException):
        board.left_end()
    with pytest.raises(EmptyBoardException):
        board.right_end()


def test_getting_left_value_domino():
    board = Board()
    # (1/2) | (2/3)
    board.add(Domino(1, 2), left=True)
    board.add(Domino(2, 3), left=False)

    current_left = board.left_end()
    
    expected_left = 1
    assert current_left == expected_left


def test_getting_right_value_domino():
    board = Board()
    # (1/2) | (2/3)
    board.add(Domino(1, 2), left=True)
    board.add(Domino(2, 3), left=False)

    current_right = board.right_end()
    
    expected_right = 3
    assert current_right == expected_right


def test_adding_wrong_domino():
    board = Board()
    # (1/2) | (2/3)
    board.add(Domino(1, 2), left=True)
    board.add(Domino(2, 3), left=False)

    with pytest.raises(EndsMismatchException):
        # (4/5) | (1/2) | (2/3)
        board.add(Domino(4, 5), left=True)

    with pytest.raises(EndsMismatchException):
        # (1/2) | (2/3) | (4/5)
        board.add(Domino(4, 5), left=False)

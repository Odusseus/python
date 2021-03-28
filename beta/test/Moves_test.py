from Moves import Moves
from Move import Move

def test_Moves():
    moves = Moves()
    assert moves.len() == 0

def test_Len_Retuen_1():
    # arrange
    moves = Moves()
    move = Move(1, 2)

    # act
    moves.append(move)

    #assert
    assert moves.len() == 1
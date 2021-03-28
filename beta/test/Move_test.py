from Move import Move

def test_Move():
    move = Move(1, 2)
    assert move.fromFieldId == 1
    assert move.toFieldId == 2
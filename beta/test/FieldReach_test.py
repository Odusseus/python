from FieldReach import FieldReach

def test_FieldReach_Default():
    fieldReach = FieldReach(1)
    assert fieldReach.id == 1
    assert fieldReach.isReached == False
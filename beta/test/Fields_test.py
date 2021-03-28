from Fields import Fields
from Field import Field

def test_Fields():
    fields = Fields()
    assert fields.len() == 0

def test_Len_Return_1():
    # arrange
    fields = Fields()
    field = Field(1)

    # act
    fields.append(field)

    #assert
    assert fields.len() == 1
import Config
import Constant
from Rook import Rook

def test_Rook_return_a_Rook():
  Config.Init(8)
  result = Rook(Constant.BLACK, Constant.ROOKBLACKCODE)
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Rook_with_field_return_a_Rook_on_a_Field():
  Config.Init(8)
  result = Rook(Constant.BLACK, Constant.ROOKBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1

def test_Rook_clone_Return_a_Clone():
    maxElement = 3
    Config.Init(maxElement)
    
    rook = Rook(Constant.WHITE, Constant.KNIGHTWHITECODE)
    result = rook.clone()
    assert result.name == rook.name
    assert result.value == rook.value
    assert result.field == rook.field #is None because is not set
    assert result.color.id == rook.color.id

    rook = Rook(Constant.WHITE, Constant.KNIGHTWHITECODE, 1)
    result = rook.clone()
    assert result.name == rook.name
    assert result.value == rook.value
    assert result.field.id == rook.field.id
    assert result.color.id == rook.color.id
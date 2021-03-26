import Config
import Constant
from Queen import Queen

def test_Queen_return_a_Queen():
  Config.Init(8)
  result = Queen(Constant.BLACK, Constant.QUEENBLACKCODE)
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Queen_with_field_return_a_Queen_on_a_Field():
  Config.Init(8)
  result = Queen(Constant.BLACK, Constant.QUEENBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1

def test_Queen_clone_Return_a_Clone():
    maxElement = 3
    Config.Init(maxElement)
    
    queen = Queen(Constant.WHITE, Constant.KNIGHTWHITECODE)
    result = queen.clone()
    assert result.name == queen.name
    assert result.value == queen.value
    assert result.field == queen.field #is None because is not set
    assert result.color.id == queen.color.id

    queen = Queen(Constant.WHITE, Constant.KNIGHTWHITECODE, 1)
    result = queen.clone()
    assert result.name == queen.name
    assert result.value == queen.value
    assert result.field.id == queen.field.id
    assert result.color.id == queen.color.id
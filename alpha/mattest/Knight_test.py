import Config
import Constant
from Knight import Knight

def test_Knight_return_a_Knight():
  Config.Init(8)
  result = Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE)
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Knight_with_field_return_a_Knight_on_a_Field():
  Config.Init(8)
  result = Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1

def test_Knight_clone_Return_a_Clone():
    maxElement = 3
    Config.Init(maxElement)
    
    knight = Knight(Constant.WHITE, Constant.KNIGHTWHITECODE)
    result = knight.clone()
    assert result.name == knight.name
    assert result.value == knight.value
    assert result.field == knight.field #is None because is not set
    assert result.color.id == knight.color.id

    knight = Knight(Constant.WHITE, Constant.KNIGHTWHITECODE, 1)
    result = knight.clone()
    assert result.name == knight.name
    assert result.value == knight.value
    assert result.field.id == knight.field.id
    assert result.color.id == knight.color.id
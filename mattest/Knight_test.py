import Config
import Constant
from Knight import Knight

def test_Knight_return_a_Knight():
  Config.Init(8)
  result = Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE, Constant.KNIGHTVALUE)
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Knight_with_field_return_a_Knight_on_a_Field():
  Config.Init(8)
  result = Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE, Constant.KNIGHTVALUE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
import Constant
from Knight import Knight

def test_Knight_return_a_Knight():
  result = Knight(Constant.BLACK)
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Knight_with_field_return_a_Knight_on_a_Field():
  result = Knight(Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KNIGHT
  assert result.shortName == Constant.KNIGHTSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
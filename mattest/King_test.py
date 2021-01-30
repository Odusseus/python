import Constant
from King import King

def test_King_return_a_King():
  result = King(Constant.BLACK)
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_King_with_field_return_a_King_on_a_Field():
  result = King(Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
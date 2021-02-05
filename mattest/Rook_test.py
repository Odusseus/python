import Constant
from Rook import Rook
from Config import Config

config = Config()

def test_Rook_return_a_Rook():
  result = Rook(config, Constant.BLACK)
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Rook_with_field_return_a_Rook_on_a_Field():
  result = Rook(config, Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
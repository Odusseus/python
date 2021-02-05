import Constant
from Queen import Queen
from Config import Config

config = Config()

def test_Queen_return_a_Queen():
  result = Queen(config, Constant.BLACK)
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Queen_with_field_return_a_Queen_on_a_Field():
  result = Queen(config, Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
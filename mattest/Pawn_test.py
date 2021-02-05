import Constant
from Config import Config
from Pawn import Pawn

config = Config()

def test_Pawn_return_a_Pawn():
  result = Pawn(config, Constant.BLACK)
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Pawn_with_field_return_a_Pawn_on_a_Field():
  result = Pawn(config, Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
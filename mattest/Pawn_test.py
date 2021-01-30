import Constant
from Pawn import Pawn

def test_Pawn_return_a_Pawn():
  result = Pawn(Constant.BLACK)
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Pawn_with_field_return_a_Pawn_on_a_Field():
  result = Pawn(Constant.BLACK, 1)
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.field.number == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
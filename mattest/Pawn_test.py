import Config
import Constant
from Pawn import Pawn

def test_Pawn_return_a_Pawn():
  Config.Init(8)
  result = Pawn(Constant.BLACK, Constant.PAWNBLACKCODE)
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Pawn_with_field_return_a_Pawn_on_a_Field():
  Config.Init(8)
  result = Pawn(Constant.BLACK, Constant.PAWNBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.PAWN
  assert result.shortName == Constant.PAWNSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
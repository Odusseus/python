import Config
import Constant
from Rook import Rook

def test_Rook_return_a_Rook():
  Config.Init(8)
  result = Rook(Constant.BLACK, Constant.ROOKBLACKCODE)
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Rook_with_field_return_a_Rook_on_a_Field():
  Config.Init(8)
  result = Rook(Constant.BLACK, Constant.ROOKBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.ROOK
  assert result.shortName == Constant.ROOKSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
import Config
import Constant
from Queen import Queen

def test_Queen_return_a_Queen():
  Config.Init(8)
  result = Queen(Constant.BLACK, Constant.QUEENBLACKCODE)
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Queen_with_field_return_a_Queen_on_a_Field():
  Config.Init(8)
  result = Queen(Constant.BLACK, Constant.QUEENBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.QUEEN
  assert result.shortName == Constant.QUEENSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1
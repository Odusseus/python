import Config
import Constant
from King import King

def test_King_return_a_King():
  Config.Init(8)
  result = King(Constant.BLACK, Constant.KINGBLACKCODE)
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_King_with_field_return_a_King_on_a_Field():
  Config.Init(8)
  result = King(Constant.BLACK, Constant.KINGBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1

def test_King_move_on_5():
  Config.Init(3)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 5)
  result = king.move()
  assert len(result) == 8
  assert 1 in result
  assert 2 in result
  assert 3 in result
  assert 4 in result
  assert 5 not in result
  assert 6 in result
  assert 7 in result
  assert 8 in result
  assert 9 in result

def test_King_move_on_1():
  Config.Init(3)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  result = king.move()
  assert len(result) == 3
  assert 4 in result
  assert 5 in result
  assert 2 in result
  
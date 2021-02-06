import Config
import Constant
from Bishop import Bishop

Config.Init()

def test_Bishop_return_a_Bishop():
  Config.Init()
  bishop = Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE)
  assert bishop.color.number == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME

def test_Bishop_with_field_return_a_Bishop_on_a_Field():
  Config.Init()
  bishop = Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, 1)
  assert bishop.color.number == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME
  assert bishop.field.number == 1
  assert bishop.field.color.name == Constant.BLACKNAME
  assert bishop.field.columnName == 'a'
  assert bishop.field.lineName == 1

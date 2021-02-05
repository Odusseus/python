import Constant
from Bishop import Bishop
from Config import Config

config = Config()

def test_Bishop_return_a_Bishop():
  bishop = Bishop(config, Constant.BLACK)
  assert bishop.color.number == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME

def test_Bishop_with_field_return_a_Bishop_on_a_Field():
  bishop = Bishop(config, Constant.BLACK, 1)
  assert bishop.color.number == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME
  assert bishop.field.number == 1
  assert bishop.field.color.name == Constant.BLACKNAME
  assert bishop.field.columnName == 'a'
  assert bishop.field.lineName == 1

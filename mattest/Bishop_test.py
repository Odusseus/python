import Config
import Constant
from Bishop import Bishop
from Color import Color

Config.Init()

def test_Bishop_return_a_Bishop():
  Config.Init()
  bishop = Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, Constant.BISHOPVALUE)
  assert bishop.color.id == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME

def test_Bishop_with_field_return_a_Bishop_on_a_Field():
  Config.Init()
  bishop = Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, Constant.BISHOPVALUE, 1)
  assert bishop.color.id == Constant.BLACK
  assert bishop.color.name == Constant.BLACKNAME
  assert bishop.field.id == 1
  assert bishop.field.color.name == Constant.BLACKNAME
  assert bishop.field.columnName == 'a'
  assert bishop.field.lineName == 1

def test_clone():
  Config.Init()
  bishop = Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, Constant.BISHOPVALUE, 1)
  
  clone = bishop.clone()
  assert clone.color.id == bishop.color.id
  assert clone.code == bishop.code
  assert clone.name == bishop.name
  assert clone.value == bishop.value
  assert clone.field.id == bishop.field.id
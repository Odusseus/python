import Constant
from Config import Config
from Player import Player

config = Config()

def test_Player_return_a_Player():
  tom = 'Tom'
  result = Player(config, tom, Constant.BLACK)
  assert result.name == tom
  assert result.color.number == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

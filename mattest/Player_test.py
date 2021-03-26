import Config
import Constant
from Player import Player

def test_Player_return_a_Player():
  Config.Init(8)
  tom = 'Tom'
  result = Player(tom, Constant.BLACK)
  assert result.name == tom
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_Play():
  Config.Init(8)
  tom = 'Tom'
  player = Player(tom, Constant.BLACK)
  
  result = player.play()

  assert result == None
import Constant
from Color import Color

class Player:
  def __init__(self, config, name, colorCode):
   assert name != None
   assert colorCode != None
   
   self.config = config
   self.name = name
   self.color = Color(self.config, colorCode)

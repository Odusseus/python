import Constant
from Color import Color

class Player:
  def __init__(self, name, colorCode):
   assert name != None
   assert colorCode != None
   
   self.name = name
   self.color = Color(colorCode)

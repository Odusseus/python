import Constant
from Color import Color

class Player:
  def __init__(self, name, colorCode):
   self.name = name
   self.color = Color(colorCode)

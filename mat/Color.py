import Constant

class Color:
  def __init__(self, number):
    assert number != None 

    self.number = number
    if(number == 0):
     self.name = Constant.BLACKNAME
    else:
     self.name = Constant.WHITENAME
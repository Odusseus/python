import Constant

class Color:
  def __init__(self, config, number):
    assert config != None 
    assert number != None 

    self.config = config
    self.number = number
    if(number == 0):
     self.name = Constant.BLACKNAME
    else:
     self.name = Constant.WHITENAME
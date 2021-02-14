import Constant

class Color:
  def __init__(self, id):
    assert id != None 

    self.id = id
    if(id == 0):
     self.name = Constant.BLACKNAME
    else:
     self.name = Constant.WHITENAME
import Constant

class Color:
  def __init__(self, id):
    assert id != None 

    self.id = id
    if(id == Constant.BLACK):
     self.name = Constant.BLACKNAME
    elif (id == Constant.WHITE):
     self.name = Constant.WHITENAME
    else:
     message = f'Color {id} is not found.'
     raise KeyError(message)

  def getOpposite(self):
    if(self.id == Constant.WHITE):
     return Color(Constant.BLACK)
    elif (self.id == Constant.BLACK):
     return Color(Constant.WHITE)
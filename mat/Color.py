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
    self.id = id
    if(id == Constant.WHITE):
     return Color(Constant.BLACK)
    elif (id == Constant.BLACK):
     return Color(Constant.WHITE)
    else:
     message = f'Color {id} is not found.'
     raise KeyError(message)
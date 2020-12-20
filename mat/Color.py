class Color:
  def __init__(self, number):
    self.number = number
    if(number == 0):
     self.name = 'Black'
    else:
     self.name = 'White'
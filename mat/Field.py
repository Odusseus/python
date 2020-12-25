import Common
from Color import Color

class Field:
  def __init__(self, number):
    self.number = number
    if (number % 2 == 0) : 
      self.color = Color(1) 
    else:
     self.color = Color(0)
    
    self.columnName = Common.numberToColumnName(number, 8)
    self.lineName = Common.numberToLineNumber(number, 8)

  def name(self):
    return self.columnName + str(self.lineName)
  

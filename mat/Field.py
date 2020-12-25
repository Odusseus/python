import math
import Constant
import Common
from Color import Color

class Field:
  def __init__(self, number):
    self.number = number
    self.color = self.numberToColor(self.number)
    self.columnName = Common.numberToColumnName(number, Constant.MAX_ELEMENT)
    self.lineName = Common.numberToLineNumber(number, Constant.MAX_ELEMENT)

  def name(self):
    return self.columnName + str(self.lineName)

  def numberToColor(self, number):
    lineNumber = math.ceil(number/Constant.MAX_ELEMENT)
    lineParity = lineNumber % 2

    if (number % 2 == 0) :
      if lineParity == 0:
        color = Color(0) 
      else:
        color = Color(1)
    else:
      if lineParity == 0:
        color = Color(1) 
      else:
        color = Color(0)
    return color
  

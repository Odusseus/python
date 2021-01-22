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
    self.name = self.columnName + str(self.lineName)
    self.piece = None

  def numberToColor(self, number, maxElement = Constant.MAX_ELEMENT):
    lineNumber = math.ceil(number/maxElement)
    if maxElement % 2 == 1:
      maxElementOdd = True
    else:
      maxElementOdd = False

    if lineNumber % 2 == 1:
      lineOdd = True
    else:
      lineOdd = False

    if number % 2 == 1:
      numberOdd = True
    else:
      numberOdd = False

    if maxElementOdd:
      if lineOdd:
        if numberOdd:
          color = Color(Constant.BLACK)
        else:
          color = Color(Constant.WHITE)
      else:
        if numberOdd:
          color = Color(Constant.WHITE) 
        else:
          color = Color(Constant.BLACK)
    else:
      if lineOdd:
        if numberOdd:
          color = Color(Constant.BLACK)
        else:
          color = Color(Constant.WHITE)
      else:
        if numberOdd:
          color = Color(Constant.WHITE) 
        else:
          color = Color(Constant.BLACK)
    return color
  
  def setPiece(self, piece):
    self.piece = piece

  def removePiece(self):
    self.piece = None
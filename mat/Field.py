import math
import Constant
import Common
from Color import Color
#from Board import Board

class Field:
  def __init__(self, config, number):
    assert config != None
    assert number != None

    self.config = config
    self.number = number
    self.color = self.numberToColor(self.number)
    self.columnName = Common.numberToColumnName(number, self.config.maxElement)
    self.lineName = Common.numberToLineNumber(number, self.config.maxElement)
    self.name = self.columnName + str(self.lineName)
    self.piece = None

  def numberToColor(self, number):
    lineNumber = math.ceil(number/self.config.maxElement)
    if self.config.maxElement % 2 == 1:
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
      if numberOdd:
        color = Color(self.config, Constant.BLACK)
      else:
        color = Color(self.config, Constant.WHITE)
      # if lineOdd:
      #   if numberOdd:
      #     color = Color(Constant.BLACK)
      #   else:
      #     color = Color(Constant.WHITE)
      # else:
      #   if numberOdd:
      #     color = Color(Constant.WHITE) 
      #   else:
      #     color = Color(Constant.BLACK)
    else:
      if lineOdd:
        if numberOdd:
          color = Color(self.config, Constant.BLACK)
        else:
          color = Color(self.config, Constant.WHITE)
      else:
        if numberOdd:
          color = Color(self.config, Constant.WHITE) 
        else:
          color = Color(self.config, Constant.BLACK)
    return color
  
  def setPiece(self, piece):
    self.piece = piece

  def removePiece(self):
    self.piece = None

  def getLastElement(self):
    return self.config.maxElement * self.config.maxElement

  def getFirstElement(self):
    return 1

  def isFilednumberInRange(self, fieldNumber):
    if fieldNumber < self.getFirstElement or fieldNumber > self.getLastElement:
      return False
    else:
      return True

  def getFieldnumberUp(self, fieldnumber):
    upNumber = fieldnumber + self.config.maxElement
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberUpRight(self, fieldnumber):
    upNumber = fieldnumber + self.config.maxElement + 1
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberUpLeft(self, fieldnumber):
    upNumber = fieldnumber + self.config.maxElement - 1
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberDown(self, fieldnumber):
    downNumber = fieldnumber - self.config.maxElement
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberDownRight(self, fieldnumber):
    downNumber = fieldnumber - self.config.maxElementElement - 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberDownLeft(self, fieldnumber):
    downNumber = fieldnumber - self.config.maxElement + 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberLeft(self, fieldnumber):
    downNumber = fieldnumber -  1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberRight(self, fieldnumber):
    downNumber = fieldnumber + 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber
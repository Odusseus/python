import math
import Config
import Constant
import Common
from Color import Color

class Field:
  def __init__(self, number):
    assert number != None

    self.number = number
    self.color = self.numberToColor(self.number)
    self.columnName = Common.numberToColumnName(number, Config.maxElement)
    self.lineName = Common.numberToLineNumber(number, Config.maxElement)
    self.name = self.columnName + str(self.lineName)
    self.piece = None

  def numberToColor(self, number):
    lineNumber = math.ceil(number/Config.maxElement)
    if Config.maxElement % 2 == 1:
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
        color = Color(Constant.BLACK)
      else:
        color = Color(Constant.WHITE)
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

  def getLastElement(self):
    return Config.maxElement * Config.maxElement

  def getFirstElement(self):
    return 1

  def isFilednumberInRange(self, fieldNumber):
    if fieldNumber < self.getFirstElement() or fieldNumber > self.getLastElement():
      return False
    else:
      return True

  def getFieldnumberUp(self, fieldnumber):
    upNumber = fieldnumber + Config.maxElement
    if not self.isFilednumberInRange(upNumber):
      return False, None
    else:
      return True, upNumber

  def getFieldnumberUpRight(self, fieldnumber):
    upNumber = fieldnumber + Config.maxElement + 1
    if not self.isFilednumberInRange(upNumber):
      return False, None
    else:
      return True, upNumber

  def getFieldnumberUpLeft(self, fieldnumber):
    upNumber = fieldnumber + Config.maxElement - 1
    if not self.isFilednumberInRange(upNumber):
      return False, None
    else:
      return True, upNumber

  def getFieldnumberDown(self, fieldnumber):
    downNumber = fieldnumber - Config.maxElement
    if not self.isFilednumberInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldnumberDownRight(self, fieldnumber):
    downNumber = fieldnumber - Config.maxElement - 1 
    if not self.isFilednumberInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldnumberDownLeft(self, fieldnumber):
    downNumber = fieldnumber - Config.maxElement + 1 
    if not self.isFilednumberInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldnumberLeft(self, fieldnumber):
    downNumber = fieldnumber -  1 
    if not self.isFilednumberInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldnumberRight(self, fieldnumber):
    downNumber = fieldnumber + 1 
    if not self.isFilednumberInRange(downNumber):
      return False, None
    else:
      return True, downNumber
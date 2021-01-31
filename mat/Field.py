import math
import Constant
import Common
from Color import Color
#from Board import Board

class Field:
  def __init__(self, number):
    assert number != None

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

  def getLastElement(self, maxElement = Constant.MAX_ELEMENT):
    return maxElement * maxElement

  def getFirstElement(self):
    return 1

  def isFilednumberInRange(self, fieldNumber):
    if fieldNumber < self.getFirstElement or fieldNumber > self.getLastElement:
      return False
    else:
      return True

  def getFieldnumberUp(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    upNumber = fieldnumber + maxElement
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberUpRight(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    upNumber = fieldnumber + maxElement + 1
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberUpLeft(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    upNumber = fieldnumber + maxElement - 1
    if not self.isFilednumberInRange(upNumber):
      return None
    else:
      return upNumber

  def getFieldnumberDown(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    downNumber = fieldnumber - maxElement
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberDownRight(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    downNumber = fieldnumber - maxElement - 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberDownLeft(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    downNumber = fieldnumber - maxElement + 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberLeft(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    downNumber = fieldnumber -  1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber

  def getFieldnumberRight(self, fieldnumber, maxElement=Constant.MAX_ELEMENT):
    downNumber = fieldnumber + 1 
    if not self.isFilednumberInRange(downNumber):
      return None
    else:
      return downNumber
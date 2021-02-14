import math
import Config
import Constant
import Common
from Color import Color

class Field:
  def __init__(self, id):
    assert id != None

    self.id = id
    self.color = self.idToColor(self.id)
    self.columnName = Common.idToColumnName(id, Config.maxElement)
    self.lineName = Common.idToLineNumber(id, Config.maxElement)
    self.name = self.columnName + str(self.lineName)
    self.piece = None

  def idToColor(self, id):
    lineId = math.ceil(id/Config.maxElement)
    if Config.maxElement % 2 == 1:
      maxElementOdd = True
    else:
      maxElementOdd = False

    if lineId % 2 == 1:
      lineOdd = True
    else:
      lineOdd = False

    if id % 2 == 1:
      idOdd = True
    else:
      idOdd = False

    if maxElementOdd:
      if idOdd:
        color = Color(Constant.BLACK)
      else:
        color = Color(Constant.WHITE)
    else:
      if lineOdd:
        if idOdd:
          color = Color(Constant.BLACK)
        else:
          color = Color(Constant.WHITE)
      else:
        if idOdd:
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

  def isFieldIdInRange(self, fieldId):
    if (fieldId == None
        or fieldId < self.getFirstElement() 
        or fieldId > self.getLastElement()):
      return False
    else:
      return True

  def getFieldIdUp(self, fieldId):
    upId = fieldId + Config.maxElement
    if not self.isFieldIdInRange(upId):
      return False, None
    else:
      return True, upId

  def getFieldIdUpRight(self, fieldId):
    upId = fieldId + Config.maxElement + 1
    if not self.isFieldIdInRange(upId):
      return False, None
    else:
      return True, upId

  def getFieldIdUpLeft(self, fieldId):
    upId = fieldId + Config.maxElement - 1
    if not self.isFieldIdInRange(upId):
      return False, None
    else:
      return True, upId

  def getFieldIdDown(self, fieldId):
    downNumber = fieldId - Config.maxElement
    if not self.isFieldIdInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldIdDownRight(self, fieldId):
    downNumber = fieldId - Config.maxElement + 1 
    if not self.isFieldIdInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldIdDownLeft(self, fieldId):
    downNumber = fieldId - Config.maxElement - 1 
    if not self.isFieldIdInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldIdLeft(self, fieldId):
    downNumber = fieldId -  1 
    column = downNumber % Config.maxElement
    if column == 0:
      downNumber = 0
    if not self.isFieldIdInRange(downNumber):
      return False, None
    else:
      return True, downNumber

  def getFieldIdRight(self, fieldId):
    column = fieldId % Config.maxElement
    downNumber = None 
    if column != 0:
      downNumber = fieldId + 1 
    if not self.isFieldIdInRange(downNumber):
      return False, None
    else:
      return True, downNumber
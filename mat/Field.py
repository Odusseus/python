import math
import Config
import Constant
import Common
from FieldReatch import FieldReatch
from Color import Color

class Field:
  def __init__(self, id):
    assert id != None

    self.id = id
    self.color = self.idToColor()
    self.columnName = Common.idToColumnName(id, Config.maxElement)
    self.lineName = Common.idToLineNumber(id, Config.maxElement)
    self.name = self.columnName + str(self.lineName)
    self.piece = None
    self.isTop = self.setIsTop()
    self.isRight = self.setIsRight()
    self.isBottom = self.setIsBottom()
    self.isLeft = self.setIsLeft()

  def idToColor(self, id = None):
    if id == None:
      id = self.id
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
    if self.isTop:
      return FieldReatch(None, False)

    upId = fieldId + Config.maxElement
    if not self.isFieldIdInRange(upId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(upId, True)

  def getFieldIdUpRight(self, fieldId):
    if self.isTop or self.isRight:
      return FieldReatch(None, False)

    upId = fieldId + Config.maxElement + 1
    if not self.isFieldIdInRange(upId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(upId, True)

  def getFieldIdUpLeft(self, fieldId):
    if self.isTop or self.isLeft:
      return FieldReatch(None, False)

    upId = fieldId + Config.maxElement - 1
    if not self.isFieldIdInRange(upId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(upId, True)

  def getFieldIdDown(self, fieldId):
    if self.isBottom:
      return FieldReatch(None, False)

    downId = fieldId - Config.maxElement
    if not self.isFieldIdInRange(downId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(downId, True)

  def getFieldIdDownRight(self, fieldId):
    if self.isBottom or self.isRight:
      return FieldReatch(None, False)

    downId = fieldId - Config.maxElement + 1 
    if not self.isFieldIdInRange(downId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(downId, True)

  def getFieldIdDownLeft(self, fieldId):
    if self.isBottom or self.isLeft:
      return FieldReatch(None, False)

    downId = fieldId - Config.maxElement - 1 
    if not self.isFieldIdInRange(downId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(downId, True)

  def getFieldIdLeft(self, fieldId):
    if self.isLeft:
      return FieldReatch(None, False)

    downId = fieldId -  1 
    column = downId % Config.maxElement
    if column == 0:
      downId = 0
    if not self.isFieldIdInRange(downId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(downId, True)

  def getFieldIdRight(self, fieldId):
    if self.isRight:
      return FieldReatch(None, False)

    column = fieldId % Config.maxElement
    downId = None 
    if column != 0:
      downId = fieldId + 1 
    if not self.isFieldIdInRange(downId):
      return FieldReatch(None, False)
    else:
      return FieldReatch(downId, True)

  def setIsTop(self, id = None):
    if id == None:
      id = self.id
    
    maxTopFieldId = Config.maxElement * Config.maxElement
    minTopFieldId = maxTopFieldId - Config.maxElement + 1

    if id >= minTopFieldId and id <= maxTopFieldId:
      return True
    else:
      return False
  
  def setIsBottom(self, id = None):
    if id == None:
      id = self.id
    
    maxTopFieldId = Config.maxElement
    minTopFieldId = 1

    if id >= minTopFieldId and id <= maxTopFieldId:
      return True
    else:
      return False

  def setIsRight(self, id = None):
    if id == None:
      id = self.id
    
    maxFieldId = Config.maxElement * Config.maxElement
    columnId = id % Config.maxElement

    if id > 0 and id <= maxFieldId and columnId == 0:
      return True
    else:
      return False

  def setIsLeft(self, id = None):
    if id == None:
      id = self.id
    
    maxFieldId = Config.maxElement * Config.maxElement
    columnId = id % Config.maxElement

    if id == 1 or (id > 0 and id <= maxFieldId and columnId == 1):
      return True
    else:
      return False
import math
import Config
import Constant
import Common
from Color import Color
from FieldReach import FieldReach

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
    self.value = 0
    self.blackValue = 0
    self.whiteValue = 0

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

  def isFieldIdInRange(self, fieldId):
    if (fieldId == None
        or fieldId < Config.minFieldId 
        or fieldId > Config.maxFieldId):
      return False
    else:
      return True

  def getFieldIdUp(self):
    if self.isTop:
      return FieldReach(None, False)

    upId = self.id + Config.maxElement
    return FieldReach(upId, True)

  def getFieldIdUpRight(self):
    if self.isTop or self.isRight:
      return FieldReach(None, False)

    upId = self.id + Config.maxElement + 1
    return FieldReach(upId, True)

  def getFieldIdUpLeft(self):
    if self.isTop or self.isLeft:
      return FieldReach(None, False)

    upId = self.id + Config.maxElement - 1
    return FieldReach(upId, True)

  def getFieldIdDown(self):
    if self.isBottom:
      return FieldReach(None, False)

    downId = self.id - Config.maxElement
    return FieldReach(downId, True)

  def getFieldIdDownRight(self):
    if self.isBottom or self.isRight:
      return FieldReach(None, False)

    downId = self.id - Config.maxElement + 1 
    return FieldReach(downId, True)

  def getFieldIdDownLeft(self):
    if self.isBottom or self.isLeft:
      return FieldReach(None, False)

    downId = self.id - Config.maxElement - 1 
    return FieldReach(downId, True)

  def getFieldIdLeft(self):
    if self.isLeft:
      return FieldReach(None, False)

    downId = self.id -  1 
    return FieldReach(downId, True)

  def getFieldIdRight(self):
    if self.isRight:
      return FieldReach(None, False)

    column = self.id % Config.maxElement
    downId = None 
    if column != 0:
      downId = self.id + 1 
    return FieldReach(downId, True)

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
    
    columnId = id % Config.maxElement

    if id > 0 and id <= Config.maxFieldId and columnId == 0:
      return True
    else:
      return False

  def setIsLeft(self, id = None):
    if id == None:
      id = self.id
    
    columnId = id % Config.maxElement

    if id == 1 or (id > 0 and id <= Config.maxFieldId and columnId == 1):
      return True
    else:
      return False
import Config
import Constant
from Piece import Piece

class King(Piece):
  def __init__(self, color, code, fieldId = None):
    Piece.__init__(
      self,
      Constant.KING,
      Constant.KINGSHORT,
      color,
      code,
      fieldId)

  def getFieldReatch(self, fieldId = None):
    if fieldId == None:
      fieldId = self.field.id
    reatch = []
    fieldReatch = self.field.getFieldIdUp(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)

    fieldReatch = self.field.getFieldIdUpRight(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)

    fieldReatch = self.field.getFieldIdRight(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)

    fieldReatch = self.field.getFieldIdDownRight(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)    
     
    fieldReatch = self.field.getFieldIdDown(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)

    fieldReatch = self.field.getFieldIdDownLeft(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)

    fieldReatch = self.field.getFieldIdLeft(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)
    
    fieldReatch = self.field.getFieldIdUpLeft(fieldId)
    if fieldReatch.isSet:
     reatch.append(fieldReatch.id)
    
    return reatch

  def getReatch(self):
    saveFieldId = self.field.id
    maxFiledId = Config.maxFieldId + 1
    moves = []
    for id in range(Config.minFieldId, maxFiledId):
      self.setField(id)
      fieldReatch = self.getFieldReatch(id)
      if len(fieldReatch) > 0:
        if len(moves) == 0:
          moves.append(None)
        moves.append(self.getFieldReatch(id))
    
    self.setField(saveFieldId)
    return moves
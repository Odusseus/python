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

  def move(self):
    fieldId = self.field.id
    reatch = []
    fieldReatch = self.field.getFieldIdUp(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldIdUpRight(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldIdRight(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldIdDownRight(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)    
     
    fieldReatch = self.field.getFieldIdDown(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldIdDownLeft(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldIdLeft(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    
    fieldReatch = self.field.getFieldIdUpLeft(fieldId)
    if fieldReatch != None:
     reatch.append(fieldReatch)
    
    return reatch
    
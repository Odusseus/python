import Constant
from Piece import Piece

class King(Piece):
  def __init__(self, config, color, code, fieldnumber = None):
    Piece.__init__(
      self,
      config,
      Constant.KING,
      Constant.KINGSHORT,
      color,
      code,
      fieldnumber)

  def move(self):
    fieldnumber = self.field.number
    reatch = []
    fieldReatch = self.field.getFieldnumberUp(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldnumberUpRight(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldnumberRight(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldnumberDownRight(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)    
     
    fieldReatch = self.field.getFieldnumberDown(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldnumberDownLeft(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    fieldReatch = self.field.getFieldnumberLeft(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)

    
    fieldReatch = self.field.getFieldnumberUpLeft(fieldnumber)
    if fieldReatch != None:
     reatch.append(fieldReatch)
    
    return reatch
    
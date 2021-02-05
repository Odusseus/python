import Constant
from Piece import Piece

class King(Piece):
  def __init__(self, color, fieldnumber = None):
    Piece.__init__(
      self,
      Constant.KING,
      Constant.KINGSHORT,
      color,
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
    
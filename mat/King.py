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

    
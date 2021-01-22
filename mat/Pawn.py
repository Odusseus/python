import Constant
from Piece import Piece

class Pawn(Piece):
  def __init__(self, color, fieldnumber = None):
    Piece.__init__(
      self,
      Constant.PAWN,
      Constant.PAWNSHORT,
      color,
      fieldnumber)
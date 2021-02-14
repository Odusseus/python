import Constant
from Piece import Piece

class Pawn(Piece):
  def __init__(self, color, code, fieldId = None):
    Piece.__init__(
      self,
      Constant.PAWN,
      Constant.PAWNSHORT,
      color,
      code,
      fieldId)
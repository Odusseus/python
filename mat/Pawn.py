import Constant
from Piece import Piece

class Pawn(Piece):
  def __init__(self, config, color, code, fieldnumber = None):
    Piece.__init__(
      self,
      config,
      Constant.PAWN,
      Constant.PAWNSHORT,
      color,
      code,
      fieldnumber)
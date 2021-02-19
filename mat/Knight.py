import Constant
from Piece import Piece

class Knight(Piece):
  def __init__(self, color, pieceCode, fieldId = None):
    Piece.__init__(
      self,
      Constant.KNIGHT,
      Constant.KNIGHTSHORT,
      color,
      pieceCode,
      fieldId)
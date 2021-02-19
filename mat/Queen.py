import Constant
from Piece import Piece

class Queen(Piece):
  def __init__(self, color, pieceCode, fieldId = None):
    Piece.__init__(
      self,
      Constant.QUEEN,
      Constant.QUEENSHORT,
      color,
      pieceCode,
      fieldId)
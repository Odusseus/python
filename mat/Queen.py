import Constant
from Piece import Piece

class Queen(Piece):
  def __init__(self, color, code, fieldId = None):
    Piece.__init__(
      self,
      Constant.QUEEN,
      Constant.QUEENSHORT,
      color,
      code,
      fieldId)
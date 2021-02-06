import Constant
from Piece import Piece

class Knight(Piece):
  def __init__(self, config, color, code, fieldnumber = None):
    Piece.__init__(
      self,
      config,
      Constant.KNIGHT,
      Constant.KNIGHTSHORT,
      color,
      code,
      fieldnumber)
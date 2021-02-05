import Constant
from Piece import Piece

class Knight(Piece):
  def __init__(self, config, color, fieldnumber = None):
    Piece.__init__(
      self,
      config,
      Constant.KNIGHT,
      Constant.KNIGHTSHORT,
      color,
      fieldnumber)
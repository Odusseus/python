import Constant
from Piece import Piece

class Queen(Piece):
  def __init__(self, config, color, fieldnumber = None):
    Piece.__init__(
      self,
      config,
      Constant.QUEEN,
      Constant.QUEENSHORT,
      color,
      fieldnumber)
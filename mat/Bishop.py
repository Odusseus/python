import Constant
from Piece import Piece

class Bishop(Piece):
  def __init__(self, config, colornumber, code, fieldnumber = None):
    Piece.__init__(
      self, 
      config,
      Constant.BISHOP, 
      Constant.BISHOPSHORT, 
      colornumber, 
      code,
      fieldnumber)
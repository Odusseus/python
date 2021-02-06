import Constant
from Piece import Piece

class Bishop(Piece):
  def __init__(self, colornumber, code, fieldnumber = None):
    Piece.__init__(
      self, 
      Constant.BISHOP, 
      Constant.BISHOPSHORT, 
      colornumber, 
      code,
      fieldnumber)
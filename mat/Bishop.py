import Constant
from Piece import Piece

class Bishop(Piece):
  def __init__(self, colorId, code, fieldId = None):
    Piece.__init__(
      self, 
      Constant.BISHOP, 
      Constant.BISHOPSHORT, 
      colorId, 
      code,
      fieldId)
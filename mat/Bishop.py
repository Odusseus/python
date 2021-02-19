import Constant
from Piece import Piece

class Bishop(Piece):
  def __init__(self, colorId, pieceCode, fieldId = None):
    Piece.__init__(
      self, 
      Constant.BISHOP, 
      Constant.BISHOPSHORT, 
      colorId, 
      pieceCode,
      fieldId)
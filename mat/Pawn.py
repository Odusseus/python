from Piece import Piece

class Pawn(Piece):
  def __init__(self, name, color, fieldnumber = None):
    Piece.__init__(self, name, color, fieldnumber = None)
from Piece import Piece

class King(Piece):
  def __init__(self, name, color, fieldnumber = None):
    Piece.__init__(self, name, color, fieldnumber)
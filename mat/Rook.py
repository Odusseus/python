import Constant
from Piece import Piece


class Rook(Piece):
    def __init__(self, config, color, fieldnumber=None):
        Piece.__init__(self,
                       config,
                       Constant.ROOK,
                       Constant.ROOKSHORT,
                       color,
                       fieldnumber)

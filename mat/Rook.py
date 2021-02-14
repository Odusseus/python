import Constant
from Piece import Piece


class Rook(Piece):
    def __init__(self, color, code, fieldId=None):
        Piece.__init__(self,
                       Constant.ROOK,
                       Constant.ROOKSHORT,
                       color,
                       code,
                       fieldId)

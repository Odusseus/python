import Constant
from Piece import Piece


class Rook(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None):
        Piece.__init__(self,
                       Constant.ROOK,
                       Constant.ROOKSHORT,
                       color,
                       pieceCode,
                       fieldId,
                       value
                       )

    def clone(self):
        clone = Rook(self.color.id, self.code, self.field.id, self.value)
        return clone

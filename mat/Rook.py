import Constant
from Piece import Piece


class Rook(Piece):
    def __init__(self, color, pieceCode, value=None, fieldId=None):
        Piece.__init__(self,
                       Constant.ROOK,
                       Constant.ROOKSHORT,
                       color,
                       pieceCode,
                       value,
                       fieldId
                       )

    def clone(self):
        clone = Rook(self.color.id, self.code, self.value, self.field.id)
        return clone

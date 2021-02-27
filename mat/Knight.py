import Constant
from Piece import Piece


class Knight(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None):
        Piece.__init__(
            self,
            Constant.KNIGHT,
            Constant.KNIGHTSHORT,
            color,
            pieceCode,
            fieldId,
            value
        )

    def clone(self):
        clone = Knight(self.color.id, self.code, self.field.id, self.value)
        return clone

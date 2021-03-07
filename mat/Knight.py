import Constant
from Piece import Piece


class Knight(Piece):
    def __init__(self, color, pieceCode, value=None, fieldId=None):
        Piece.__init__(
            self,
            Constant.KNIGHT,
            Constant.KNIGHTSHORT,
            color,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        clone = Knight(self.color.id, self.code, self.value, self.field.id)
        return clone

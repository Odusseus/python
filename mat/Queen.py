import Constant
from Piece import Piece


class Queen(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None):
        Piece.__init__(
            self,
            Constant.QUEEN,
            Constant.QUEENSHORT,
            color,
            pieceCode,
            fieldId,
            value
        )

    def clone(self):
        clone = Queen(self.color.id, self.code, self.field.id, self.value)
        return clone

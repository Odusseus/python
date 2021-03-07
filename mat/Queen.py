import Constant
from Piece import Piece


class Queen(Piece):
    def __init__(self, color, pieceCode, value=None, fieldId=None):
        Piece.__init__(
            self,
            Constant.QUEEN,
            Constant.QUEENSHORT,
            color,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        clone = Queen(self.color.id, self.code, self.value, self.field.id)
        return clone

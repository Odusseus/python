import Constant
from Piece import Piece


class Pawn(Piece):
    def __init__(self, color, pieceCode, value=None, fieldId=None):
        Piece.__init__(
            self,
            Constant.PAWN,
            Constant.PAWNSHORT,
            color,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        clone = Pawn(self.color.id, self.code, self.value, self.field.id)
        return clone

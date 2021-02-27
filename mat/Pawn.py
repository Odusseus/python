import Constant
from Piece import Piece


class Pawn(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None, ):
        Piece.__init__(
            self,
            Constant.PAWN,
            Constant.PAWNSHORT,
            color,
            pieceCode,
            fieldId,
            value
        )

    def clone(self):
        clone = Pawn(self.color.id, self.code, self.field.id, self.value)
        return clone

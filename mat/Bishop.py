import Constant
from Piece import Piece


class Bishop(Piece):
    def __init__(self, colorId, pieceCode, fieldId=None, value=None):
        Piece.__init__(
            self,
            Constant.BISHOP,
            Constant.BISHOPSHORT,
            colorId,
            pieceCode,
            fieldId,
            value
        )

    def clone(self):
        clone = Bishop(self.color, self.code, self.value, self.field.id)
        return clone

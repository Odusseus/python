import Constant
from Piece import Piece


class Bishop(Piece):
    def __init__(self, colorId, pieceCode, value=None, fieldId=None):
        Piece.__init__(
            self,
            Constant.BISHOP,
            Constant.BISHOPSHORT,
            colorId,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id

        clone = Bishop(self.color.id, self.code, self.value, id)
        return clone

import Constant
from Piece import Piece


class Pawn(Piece):
    def __init__(self, colorId, pieceCode, fieldId=None, value=None):
        assert colorId != None
        assert pieceCode != None
        if value == None:
            value = Constant.PAWNVALUE
        Piece.__init__(
            self,
            Constant.PAWN,
            Constant.PAWNSHORT,
            colorId,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        clone = Pawn(self.color.id, self.code, id, self.value)
        return clone

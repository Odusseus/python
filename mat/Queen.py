import Constant
from Piece import Piece


class Queen(Piece):
    def __init__(self, colorId, pieceCode, fieldId=None, value=None):
        assert colorId != None
        assert pieceCode != None
        if value == None:
            value = Constant.QUEENVALUE
        Piece.__init__(
            self,
            Constant.QUEEN,
            Constant.QUEENSHORT,
            colorId,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        clone = Queen(self.color.id, self.code, id, self.value)
        return clone

import Constant
from Piece import Piece


class Knight(Piece):
    def __init__(self, colorId, pieceCode, fieldId=None, value=None):
        assert colorId != None
        assert pieceCode != None
        if value == None:
            value = Constant.KNIGHTVALUE
        Piece.__init__(
            self,
            Constant.KNIGHT,
            Constant.KNIGHTSHORT,
            colorId,
            pieceCode,
            value,
            fieldId
        )

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
          
        clone = Knight(self.color.id, self.code, id, self.value)
        return clone

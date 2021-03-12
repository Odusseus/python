import Constant
from Piece import Piece


class Rook(Piece):
    def __init__(self, colorId, pieceCode, fieldId=None, value=None):
        assert colorId != None
        assert pieceCode != None
        if value == None:
            value = Constant.ROOKVALUE
        Piece.__init__(self,
                       Constant.ROOK,
                       Constant.ROOKSHORT,
                       colorId,
                       pieceCode,
                       value,
                       fieldId
                       )

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        clone = Rook(self.color.id, self.code, id, self.value)
        return clone

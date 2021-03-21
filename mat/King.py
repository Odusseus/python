#import Config
import Constant
from Piece import Piece


class King(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None):
        assert color != None
        assert pieceCode != None
        if value == None:
            value = Constant.KINGVALUE
        Piece.__init__(
            self,
            Constant.KING,
            Constant.KINGSHORT,
            color,
            pieceCode,
            value,
            fieldId
        )

    def getFieldReach(self, fieldId=None):
        if fieldId == None:
            fieldId = self.field.id
        reach = []
        fieldReach = self.field.getFieldIdUp(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdUpRight(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdRight(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdDownRight(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdDown(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdDownLeft(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdLeft(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        fieldReach = self.field.getFieldIdUpLeft(fieldId)
        if fieldReach.isSet:
            reach.append(fieldReach.id)

        return reach

    # TODO clean up
    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        clone = King(self.color.id, self.code, id, self.value)
        return clone

    def setCurrentReachs(self, pieces):
        reachs = self.getReachs()
        if pieces == None:
            self.currentReachs = reachs
            return

        currentReachs = []
        for reach in reachs:
          add = True
          for piece in pieces:
            if reach == piece.field.id and piece.color.id == self.color.id:
              add = False
          if add: 
            currentReachs.append(reach)
        self.currentReachs = currentReachs


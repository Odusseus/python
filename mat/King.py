#import Config
import Constant
from Piece import Piece


class King(Piece):
    def __init__(self, color, pieceCode, fieldId=None, value=None):
        Piece.__init__(
            self,
            Constant.KING,
            Constant.KINGSHORT,
            color,
            pieceCode,
            fieldId,
            value
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

    def clone(self):
        clone = King(self.color.id, self.code, self.field.id, self.value)
        return clone

    def setCurrentReachs(self, pieces):
        currentReachs = []
        for reach in self.reachs:
            for piece in pieces:
                if piece.field.id != reach:
                    currentReachs.append(reach)
        self.currentReachs = currentReachs

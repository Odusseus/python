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

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        
        piece = King(self.color.id, self.code, id, self.value)
        return piece

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


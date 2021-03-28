import numbers
import Config
import Constant
from collections import deque
from abc import ABC, abstractmethod
from Color import Color
from Field import Field
from Board import Board

class Piece(ABC):

    def __init__(self, name, shortName, colorId, pieceCode, value, fieldId_or_fieldstring=None):
        assert name != None
        assert shortName != None
        assert colorId != None
        assert pieceCode != None
        assert value != None

        self.board = Board()
        self.board.setFieldsValue()
        Config.maxPiece += 1
        self.id = Config.maxPiece
        self.name = name
        self.shortName = shortName
        self.color = Color(colorId)
        self.code = pieceCode
        self.field = None
        self.setField(fieldId_or_fieldstring)
        self.shortNameColor = self.shortName + self.color.name[0].lower()
        self.reachs = []
        self.currentReachs = []
        self.value = value
        self.powerValue = None

    def clone(self):
        id = None
        if self.field != None:
          id = self.field.id
        
        piece = Piece(self.name, self.shortName, self.color.id, self.code, self.value, id)
        return piece

    def setField(self, fieldId_or_fieldstring=None):
        if fieldId_or_fieldstring == None:
            self.field = None
            return
        else:
            if isinstance(fieldId_or_fieldstring, numbers.Number):
                fieldId = fieldId_or_fieldstring
            else:
                fieldId = self.board.fieldnames.get(fieldId_or_fieldstring)
                if fieldId == None:
                    message = f'{fieldId_or_fieldstring} is not found'
                    raise KeyError(message)
        self.field = Field(fieldId)

    def getFieldReach(self, fieldId ):
        raise Exception("Piece.getFieldReach not implementeted")
        # reach = []
        # if self.reachs != None:
        #   reach = self.reachs[fieldId]
        # return reach

    def setReachs(self):
        if self.field == None or self.field.id == None:
            return
        saveFieldId = self.field.id
        maxFiledId = Config.maxFieldId + 1
        moves = []
        for id in range(Config.minFieldId, maxFiledId):
            self.setField(id)
            fieldReatch = self.getFieldReach(id)
            if len(fieldReatch) > 0:
                if len(moves) == 0:
                    moves.append(None)
                moves.append(self.getFieldReach(id))
        # self.reachs = moves
        for move in moves:
            self.reachs.append(move)
        self.setField(saveFieldId)

    def getAllReachs(self):
        if self.reachs == None or len(self.reachs) == 0:
            self.setReachs()
        return self.reachs

    def getReachs(self):
        if self.reachs != None and len(self.reachs) != 0:
            id = 0
            if isinstance(self.field.id, int):
                id = self.field.id
            reachs = self.reachs[id]
            return reachs
        return []

    def setValue(self, value=None):
        if value != None:
            self.value = value
        else:
            if self.name == Constant.KING:
                self.value = Constant.KINGVALUE
            elif self.name == Constant.QUEEN:
                self.value = Constant.QUEENVALUE
            elif self.name == Constant.ROOK:
                self.value = Constant.ROOKVALUE
            elif self.name == Constant.BISHOP:
                self.value = Constant.BISHOPVALUE
            elif self.name == Constant.KNIGHT:
                self.value = Constant.KNIGHTVALUE
            elif self.name == Constant.PAWN:
                self.value = Constant.PAWNVALUE         

    # def setCurrentReachs(self, pieces):
    #     self.currentReachs = []
    
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

    def getCurrentReachs(self):
        return self.currentReachs   

    def setPowerValue(self):
        self.powerValue = self.value
        for field in self.reachs:
            if field == None:
                continue

            for fieldId in field:
                value = self.board.fields[fieldId].value
                self.powerValue += value

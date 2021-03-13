import Config
import Constant
from Field import Field
from Move import Move
from Color import Color


class Board:

    def __init__(self, deep=0, name=Constant.DEFAULT):
        self.maxElement = Config.maxElement
        self.maxLine = self.maxElement
        self.maxColumn = self.maxElement
        self.name = name
        self.deep = deep + 1
        self.fields = []
        for i in range(1, self.getMaxField() + 1):
            if i == 1:
                self.fields.append(Field(0))  # Field 0 doesn't exist
            self.fields.append(Field(i))

        self.fieldnames = {}
        for field in self.fields:
            self.fieldnames[field.name] = field.id

        self.whitePieces = []
        self.blackPieces = []
        self.moves = []
        self.lastMove = None

    def getMaxField(self):
        return self.maxLine * self.maxColumn

    def setPiece(self, piece):        
        if piece.color.id == Constant.WHITE:
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)
        self.fields[piece.field.id].piece = piece

    def cleanField(self, fieldId):
        self.fields[fieldId].piece = None

    def deletePiece(self, piece):
        if piece.color.id == Constant.WHITE:
            self.whitePieces = [
                piece for piece in self.whitePieces if piece.id != piece.id]
        else:
            self.blackPieces = [
                piece for piece in self.blackPieces if piece.id != piece.id]
        self.fields[piece.field.id].piece = None

    def getPieces(self, color):
        if color.id == Constant.WHITE:
            return self.whitePieces
        else:
            return self.blackPieces

    def getAllPieces(self):
        allPieces = self.whitePieces + self.blackPieces
        return allPieces

    def getKing(self, colorId):
        if colorId == Constant.WHITE:
            pieces = self.whitePieces
        else:
            pieces = self.blackPieces
        for piece in pieces:
          if piece.name == Constant.KING:
            return piece

    def clone(self):
        board = Board(self.deep, self.name)
        pieces = self.getAllPieces()
        for piece in pieces:
            clone = piece.clone()
            clone.setReachs()
            board.setPiece(clone)
        board.setCurrentReachs()
        return board

    def setCurrentReachs(self):
        pieces = self.getAllPieces()
        for piece in pieces:
            piece.setCurrentReachs(pieces)

    def play(self, move):
        piece = self.fields[move.fromFieldId].piece
        if(self.fields[move.toFieldId].piece != None
           and self.fields[move.fromFieldId].piece.color.id == self.fields[move.toFieldId].piece.color.id):
            message = f'{move.fromFieldId} and {move.toFieldId} have the same piece color.'
            raise Exception(message)
        if(self.fields[move.toFieldId].piece != None
           and self.fields[move.fromFieldId].piece.color.id != self.fields[move.toFieldId].piece.color.id):
            self.deletePiece(self.fields[move.toFieldId].piece)
        piece.setField(move.toFieldId)
        self.fields[move.toFieldId].piece = piece
        self.cleanField(move.fromFieldId)
        self.lastMove = move
        self.moves.append(move)
        self.setCurrentReachs()

    def isCheck(self, colorId):
        king = self.getKing(colorId)
        if (colorId == Constant.WHITE):
            colorBlack = Color(Constant.BLACK)
            opponentPieces = self.getPieces(colorBlack)
        else:
            colorWhite = Color(Constant.WHITE)
            opponentPieces = self.getPieces(colorWhite)
        isCheck = False
        for piece in opponentPieces:
            #if piece
            currentReachs = piece.getCurrentReachs()
            for reach in currentReachs:
                if king.field.id == reach:
                    return True
        return isCheck

    def evaluate(self):
        # for piece in self.getAllPieces():
        #     if piece.color.id == Constant.WHITE:
        #         piece.setCurrentReachs(self.whitePieces)
        #     else:
        #         piece.setCurrentReachs(self.blackPieces)

        value = 0
        for piece in self.getAllPieces():
            if piece.color.id == Constant.WHITE:
                value += piece.value
            else:
                value -= piece.value
        self.value = value

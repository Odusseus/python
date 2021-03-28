import Config
import Constant
from Field import Field


class Board:

    def __init__(self, deep=0, name=Constant.DEFAULT):
        self.maxElement = Config.maxElement
        self.maxLine = self.maxElement
        self.maxColumn = self.maxElement
        self.name = name
        self.deep = deep + 1
        self.fields = []
        for i in range(1, self.getMaxField()):
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
        return (self.maxLine * self.maxColumn) + 1

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
                whitePiece for whitePiece in self.whitePieces if whitePiece.id != piece.id]
        else:
            self.blackPieces = [
                blackPiece for blackPiece in self.blackPieces if blackPiece.id != piece.id]
        self.fields[piece.field.id].piece = None

    def getPieces(self, colorId):
        if colorId == Constant.WHITE:
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
        for field in self.fields:
            board.fields[field.id].value = field.value
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
            opponentPieces = self.getPieces(Constant.BLACK)
        else:
            opponentPieces = self.getPieces(Constant.WHITE)
        isCheck = False
        for piece in opponentPieces:
            # if piece
            currentReachs = piece.getCurrentReachs()
            for reach in currentReachs:
                if king.field.id == reach:
                    return True
        return isCheck

    def evaluate(self):
        value = 0
        for piece in self.getAllPieces():
            if piece.color.id == Constant.WHITE:
                value += piece.value
            else:
                value -= piece.value
        self.value = value

    def setFieldsValue(self):
        line = 1
        column = 1
        lineValue = 0
        middleUp = int(self.maxLine / 2) + 1
        middleDown = int(self.maxLine / 2)

        for line in range(self.maxLine):
            if line < middleDown:
                lineValue += 1
            elif line >= middleUp:
                lineValue -= 1
            columnValue = 0
            for column in range(1, self.maxColumn + 1):
                if column <= middleDown:
                    columnValue += 1
                elif column > middleUp:
                    columnValue -= 1
                fieldId = (line * self.maxColumn) + column
                self.fields[fieldId].value = lineValue + columnValue

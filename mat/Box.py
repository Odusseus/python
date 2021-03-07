import Constant
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn

class Box:
  def __init__(self):
    True == True

  def getKingBlack(self, fieldId = None):
     piece = King(Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, fieldId)
     piece.setReachs()
     return piece

  def getQueenBlack(self, fieldId = None):
    return Queen(Constant.BLACK, Constant.QUEENBLACKCODE, Constant.QUEENVALUE, fieldId)

  def getRookBlack(self, fieldId = None):
    return Rook(Constant.BLACK, Constant.ROOKBLACKCODE, Constant.ROOKVALUE, fieldId)

  def getBishopBlack(self, fieldId = None):
    return Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, Constant.BISHOPVALUE, fieldId)

  def getKnightBlack(self, fieldId = None):
    return Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE, Constant.KNIGHTVALUE, fieldId)

  def getPawnBlack(self, fieldId = None):
    return Pawn(Constant.BLACK, Constant.PAWNBLACKCODE, Constant.PAWNVALUE, fieldId)

  def getKingWhite(self, fieldId = None):    
    piece = King(Constant.WHITE, Constant.KINGWHITECODE, Constant.KINGVALUE, fieldId)
    piece.setReachs()
    return piece

  def getQueenWhite(self, fieldId = None):
    return Queen(Constant.WHITE, Constant.QUEENWHITECODE, Constant.QUEENVALUE, fieldId)

  def getRookWhite(self, fieldId = None):
    return Rook(Constant.WHITE, Constant.ROOKWHITECODE, Constant.ROOKVALUE, fieldId)

  def getBishopWhite(self, fieldId = None):
    return Bishop(Constant.WHITE, Constant.BISHOPWHITECODE, Constant.BISHOPVALUE, fieldId)

  def getKnightWhite(self, fieldId = None):
    return  Knight(Constant.WHITE, Constant.KNIGHTWHITECODE, Constant.KNIGHTVALUE, fieldId)

  def getPawnWhite(self, fieldId = None):
    return Pawn(Constant.WHITE, Constant.PAWNWHITECODE, Constant.PAWNVALUE, fieldId)
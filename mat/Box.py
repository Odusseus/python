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
     return King(Constant.BLACK, Constant.KINGBLACKCODE, fieldId)

  def getQueenBlack(self, fieldId = None):
    return Queen(Constant.BLACK, Constant.QUEENBLACKCODE, fieldId)

  def getRookBlack(self, fieldId = None):
    return Rook(Constant.BLACK, Constant.ROOKBLACKCODE, fieldId)

  def getBishopBlack(self, fieldId = None):
    return Bishop(Constant.BLACK, Constant.BISHOPBLACKCODE, fieldId)

  def getKnightBlack(self, fieldId = None):
    return Knight(Constant.BLACK, Constant.KNIGHTBLACKCODE, fieldId)

  def getPawnBlack(self, fieldId = None):
    return Pawn(Constant.BLACK, Constant.PAWNBLACKCODE, fieldId)

  def getKingWhite(self, fieldId = None):    
    return King(Constant.WHITE, Constant.KINGWHITECODE, fieldId)

  def getQueenWhite(self, fieldId = None):
    return Queen(Constant.WHITE, Constant.QUEENWHITECODE, fieldId)

  def getRookWhite(self, fieldId = None):
    return Rook(Constant.WHITE, Constant.ROOKWHITECODE, fieldId)

  def getBishopWhite(self, fieldId = None):
    return Bishop(Constant.WHITE, Constant.BISHOPWHITECODE, fieldId)

  def getKnightWhite(self, fieldId = None):
    return  Knight(Constant.WHITE, Constant.KNIGHTWHITECODE, fieldId)

  def getPawnWhite(self, fieldId = None):
    return Pawn(Constant.WHITE, Constant.PAWNWHITECODE, fieldId)
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

  def getKingBlack(self, fieldnumber = None):
     return King(Constant.KING, Constant.BLACK, fieldnumber)

  def getQueenBlack(self, fieldnumber = None):
    return Queen(Constant.QUEEN, Constant.BLACK, fieldnumber)

  def getRookBlack(self, fieldnumber = None):
    return Rook(Constant.ROOK, Constant.BLACK, fieldnumber)

  def getBishopBlack(self, fieldnumber = None):
    return Bishop(Constant.BISHOP, Constant.BLACK, fieldnumber)

  def getKnightBlack(self, fieldnumber = None):
    return Knight(Constant.KNIGHT, Constant.BLACK, fieldnumber)

  def getPawnBlack(self, fieldnumber = None):
    return Pawn(Constant.PAWN, Constant.BLACK, fieldnumber)

  def getKingWhite(self, fieldnumber = None):    
    return King(Constant.KING, Constant.WHITE, fieldnumber)

  def getQueenWhite(self, fieldnumber = None):
    return Queen(Constant.QUEEN, Constant.WHITE, fieldnumber)

  def getRookWhite(self, fieldnumber = None):
    return Rook(Constant.ROOK, Constant.WHITE, fieldnumber)

  def getBishopWhite(self, fieldnumber = None):
    return Bishop(Constant.BISHOP, Constant.WHITE, fieldnumber)

  def getKnightWhite(self, fieldnumber = None):
    return  Knight(Constant.KNIGHT, Constant.WHITE, fieldnumber)

  def getPawnWhite(self, fieldnumber = None):
    return Pawn(Constant.PAWN, Constant.WHITE, fieldnumber)
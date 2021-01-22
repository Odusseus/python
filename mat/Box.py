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
     return King(Constant.BLACK, fieldnumber)

  def getQueenBlack(self, fieldnumber = None):
    return Queen(Constant.BLACK, fieldnumber)

  def getRookBlack(self, fieldnumber = None):
    return Rook(Constant.BLACK, fieldnumber)

  def getBishopBlack(self, fieldnumber = None):
    return Bishop(Constant.BLACK, fieldnumber)

  def getKnightBlack(self, fieldnumber = None):
    return Knight(Constant.BLACK, fieldnumber)

  def getPawnBlack(self, fieldnumber = None):
    return Pawn(Constant.BLACK, fieldnumber)

  def getKingWhite(self, fieldnumber = None):    
    return King(Constant.WHITE, fieldnumber)

  def getQueenWhite(self, fieldnumber = None):
    return Queen(Constant.WHITE, fieldnumber)

  def getRookWhite(self, fieldnumber = None):
    return Rook(Constant.WHITE, fieldnumber)

  def getBishopWhite(self, fieldnumber = None):
    return Bishop(Constant.WHITE, fieldnumber)

  def getKnightWhite(self, fieldnumber = None):
    return  Knight(Constant.WHITE, fieldnumber)

  def getPawnWhite(self, fieldnumber = None):
    return Pawn(Constant.WHITE, fieldnumber)
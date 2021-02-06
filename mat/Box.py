import Constant
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn

class Box:
  def __init__(self, config):
    self.config = config    

  def getKingBlack(self, fieldnumber = None):
     return King(self.config, Constant.BLACK, Constant.KINGBLACKCODE, fieldnumber)

  def getQueenBlack(self, fieldnumber = None):
    return Queen(self.config, Constant.BLACK, Constant.QUEENBLACKCODE, fieldnumber)

  def getRookBlack(self, fieldnumber = None):
    return Rook(self.config, Constant.BLACK, Constant.ROOKBLACKCODE, fieldnumber)

  def getBishopBlack(self, fieldnumber = None):
    return Bishop(self.config, Constant.BLACK, Constant.BISHOPBLACKCODE, fieldnumber)

  def getKnightBlack(self, fieldnumber = None):
    return Knight(self.config, Constant.BLACK, Constant.KNIGHTBLACKCODE, fieldnumber)

  def getPawnBlack(self, fieldnumber = None):
    return Pawn(self.config, Constant.BLACK, Constant.PAWNBLACKCODE, fieldnumber)

  def getKingWhite(self, fieldnumber = None):    
    return King(self.config, Constant.WHITE, Constant.KINGWHITECODE, fieldnumber)

  def getQueenWhite(self, fieldnumber = None):
    return Queen(self.config, Constant.WHITE, Constant.QUEENWHITECODE, fieldnumber)

  def getRookWhite(self, fieldnumber = None):
    return Rook(self.config, Constant.WHITE, Constant.ROOKWHITECODE, fieldnumber)

  def getBishopWhite(self, fieldnumber = None):
    return Bishop(self.config, Constant.WHITE, Constant.BISHOPWHITECODE, fieldnumber)

  def getKnightWhite(self, fieldnumber = None):
    return  Knight(self.config, Constant.WHITE, Constant.KNIGHTWHITECODE, fieldnumber)

  def getPawnWhite(self, fieldnumber = None):
    return Pawn(self.config, Constant.WHITE, Constant.PAWNWHITECODE, fieldnumber)
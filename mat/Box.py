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
     return King(self.config, Constant.BLACK, fieldnumber)

  def getQueenBlack(self, fieldnumber = None):
    return Queen(self.config, Constant.BLACK, fieldnumber)

  def getRookBlack(self, fieldnumber = None):
    return Rook(self.config, Constant.BLACK, fieldnumber)

  def getBishopBlack(self, fieldnumber = None):
    return Bishop(self.config, Constant.BLACK, fieldnumber)

  def getKnightBlack(self, fieldnumber = None):
    return Knight(self.config, Constant.BLACK, fieldnumber)

  def getPawnBlack(self, fieldnumber = None):
    return Pawn(self.config, Constant.BLACK, fieldnumber)

  def getKingWhite(self, fieldnumber = None):    
    return King(self.config, Constant.WHITE, fieldnumber)

  def getQueenWhite(self, fieldnumber = None):
    return Queen(self.config, Constant.WHITE, fieldnumber)

  def getRookWhite(self, fieldnumber = None):
    return Rook(self.config, Constant.WHITE, fieldnumber)

  def getBishopWhite(self, fieldnumber = None):
    return Bishop(self.config, Constant.WHITE, fieldnumber)

  def getKnightWhite(self, fieldnumber = None):
    return  Knight(self.config, Constant.WHITE, fieldnumber)

  def getPawnWhite(self, fieldnumber = None):
    return Pawn(self.config, Constant.WHITE, fieldnumber)
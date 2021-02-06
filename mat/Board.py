import Config
import Constant
from Field import Field

class Board:

  def __init__(self, name = Constant.DEFAULT):
    self.maxElement = Config.maxElement
    self.maxLine = self.maxElement
    self.maxColumn = self.maxElement
    self.name = name
    self.fields = []
    for i in range(1, self.getMaxField() + 1):
      if i == 1:
        self.fields.append(Field(0)) # Field 0 doesn't exist
      self.fields.append(Field(i))
    
    self.fieldnames = {} 
    for field in self.fields:
      self.fieldnames[field.name] = field.number
    
    self.pieces= []

  def getMaxField(self):
    return self.maxLine * self.maxColumn

  def addPiece(self, piece):
    self.pieces.append(piece)
    self.fields[piece.field.number].piece = piece
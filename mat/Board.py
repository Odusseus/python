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
      self.fieldnames[field.name] = field.id
    
    self.whitePieces= []
    self.blackPieces= []

  def getMaxField(self):
    return self.maxLine * self.maxColumn

  def addPiece(self, piece):
    if piece.color.id == Constant.WHITE:
      self.whitePieces.append(piece)
    else:
      self.blackPieces.append(piece)
    self.fields[piece.field.id].piece = piece

  def getPieces(self, color):
    if color.id == Constant.WHITE:
      return self.whitePieces
    else:
      return self.blackPieces

  def getAllPieces(self):
    allPieces = self.whitePieces + self.blackPieces
    return allPieces
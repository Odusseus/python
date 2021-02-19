import numbers
import Config
from collections import deque
from Color import Color
from Field import Field
from Board import Board

class Piece:
  
  def __init__(self, name, shortName, colorId, pieceCode, fieldId_or_fieldstring = None):
    assert name != None
    assert shortName != None
    assert colorId != None
    assert pieceCode != None

    self.board = Board() 
    self.name = name
    self.shortName = shortName
    self.color = Color(colorId)
    self.code = pieceCode
    self.field = None
    self.setField(fieldId_or_fieldstring)
    self.shortNameColor = self.shortName + self.color.name[0].lower()
    self.reachs = []

  def setField(self, fieldId_or_fieldstring = None):
    if fieldId_or_fieldstring == None:
      self.field = None
      return
    else:
      if isinstance(fieldId_or_fieldstring, numbers.Number):
       fieldId = fieldId_or_fieldstring
      else:
        fieldId = self.board.fieldnames.get(fieldId_or_fieldstring)
        if fieldId == None:
          message = f'{fieldId_or_fieldstring} is not found'
          raise KeyError(message)          
    self.field = Field(fieldId)
   
  def getFieldReach(self, fieldId = None):
    if fieldId == None:
      fieldId = self.field.id
    reach = []
    return reach


  def setReachs(self):
    if self.field == None or self.field.id == None:
      return
    saveFieldId = self.field.id
    maxFiledId = Config.maxFieldId + 1
    moves = []
    for id in range(Config.minFieldId, maxFiledId):
      self.setField(id)
      fieldReatch = self.getFieldReach(id)
      if len(fieldReatch) > 0:
        if len(moves) == 0:
          moves.append(None)
        moves.append(self.getFieldReach(id))
    #self.reachs = moves
    for move in moves:
      self.reachs.append(move)
    self.setField(saveFieldId)

  def getAllReachs(self):
    if self.reachs == None or len(self.reachs) == 0:
      self.setReachs()
    return self.reachs

  def getReachs(self):
    if self.reachs != None and len(self.reachs) != 0:
      id = 0
      if isinstance(self.field.id, int):
        id = self.field.id
      reachs = self.reachs[id]
      return reachs
    return [] 
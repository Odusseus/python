import numbers
from Color import Color
from Field import Field
from Board import Board

class Piece:
  
  def __init__(self, name, shortName, colorId, code, fieldId_or_fieldstring = None):
    assert name != None
    assert shortName != None
    assert colorId != None
    assert code != None

    self.board = Board() 
    self.name = name
    self.shortName = shortName
    self.color = Color(colorId)
    self.code = code
    if fieldId_or_fieldstring == None:
      fieldId = None
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
    self.shortNameColor = self.shortName + self.color.name[0].lower()
    self.reach = []

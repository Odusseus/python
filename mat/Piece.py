import numbers
from Color import Color
from Field import Field
from Board import Board

class Piece:
  
  def __init__(self, name, shortName, colornumber, code, fieldnumber_or_fieldstring = None):
    assert name != None
    assert shortName != None
    assert colornumber != None
    assert code != None

    self.board = Board() 
    self.name = name
    self.shortName = shortName
    self.color = Color(colornumber)
    self.code = code
    if fieldnumber_or_fieldstring == None:
      fieldnumber = None
      return
    else:
      if isinstance(fieldnumber_or_fieldstring, numbers.Number):
       fieldnumber = fieldnumber_or_fieldstring
      else:
        fieldnumber = self.board.fieldnames.get(fieldnumber_or_fieldstring)
        if fieldnumber == None:
          message = f'{fieldnumber_or_fieldstring} is not found'
          raise KeyError(message)
          
    self.field = Field(fieldnumber)
    self.shortNameColor = self.shortName + self.color.name[0].lower()
    self.reach = []

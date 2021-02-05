import numbers
import Constant
from Color import Color
from Field import Field
from Board import Board

class Piece:
  
  def __init__(self, config, name, shortName, colornumber, fieldnumber_or_fieldstring = None):
    assert config != None
    assert name != None
    assert shortName != None
    assert colornumber != None

    self.config = config
    self.board = Board(self.config) 
    self.name = name
    self.shortName = shortName
    self.color = Color(self.config, colornumber)
    if fieldnumber_or_fieldstring == None:
      fieldnumber = None
      return
    else:
      if isinstance(fieldnumber_or_fieldstring, numbers.Number):
       fieldnumber = fieldnumber_or_fieldstring
      else:
        fieldnumber = self.board.fieldnames[fieldnumber_or_fieldstring]
    self.field = Field(self.config, fieldnumber)
    self.shortNameColor = self.shortName + self.color.name[0].lower()
    self.reach = []

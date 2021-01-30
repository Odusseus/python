import numbers
import Constant
from Color import Color
from Field import Field
from Board import Board

board = Board(Constant.MAX_ELEMENT)

class Piece:
  
  def __init__(self, name, shortName, colornumber, fieldnumber_or_fieldstring = None):
    assert name != None
    assert shortName != None
    assert colornumber != None

    self.name = name
    self.shortName = shortName
    self.color = Color(colornumber)
    if fieldnumber_or_fieldstring == None:
      fieldnumber = None
      return
    else:
      if isinstance(fieldnumber_or_fieldstring, numbers.Number):
       fieldnumber = fieldnumber_or_fieldstring
      else:
        fieldnumber = board.fieldnames[fieldnumber_or_fieldstring]
    self.field = Field(fieldnumber)
    self.shortNameColor = self.shortName + self.color.name[0].lower()

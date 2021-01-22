import Constant
from Color import Color
from Field import Field
from Board import Board

board = Board(Constant.MAX_ELEMENT)

class Piece:
  
  def __init__(self, name, color, fieldnumber_or_fieldstring = None):
    self.name = name
    self.color = Color(color)
    if fieldnumber_or_fieldstring == None:
      fieldnumber = None
    else:
      if type(fieldnumber_or_fieldstring) == 'int':
       fieldnumber = fieldnumber_or_fieldstring
      else:
        fieldnumber = board.fieldnames[fieldnumber_or_fieldstring]
    self.field = Field(fieldnumber)

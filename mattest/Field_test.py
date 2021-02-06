import Config
import Constant
from Field import Field   # The code to test
from Piece import Piece

def test_Field_Black_Oddline():
  Config.Init()
  field = Field(1)

  assert field.color.number == Constant.BLACK
  assert field.color.name == Constant.BLACKNAME

def test_Field_Black_evenline():
  Config.Init()
  field = Field(10)

  assert field.color.number == Constant.BLACK
  assert field.color.name == Constant.BLACKNAME

def test_Field_White_oddline():
  Config.Init()
  field = Field(2)

  assert field.color.number == Constant.WHITE
  assert field.color.name == Constant.WHITENAME

def test_Field_White_evenline():
  Config.Init()
  field = Field(9)

  assert field.color.number == Constant.WHITE
  assert field.color.name == Constant.WHITENAME

def test_setPiece():
  # Arrange
  Config.Init()
  field = Field(1)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE)
  
  # Act
  field.setPiece(piece)

  assert field.piece.name == Constant.KING

def test_removePiece():
  # Arrange
  Config.Init()
  field = Field(1)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE)
  field.setPiece(piece)

  # Act
  field.removePiece()

  assert field.piece == None


def test_numberToColor():
  Config.Init()
  field = Field(1)
  assert field.numberToColor(1).number == 0
  assert field.numberToColor(2).number == 1
  assert field.numberToColor(3).number == 0
  assert field.numberToColor(4).number == 1
  assert field.numberToColor(5).number == 0
  assert field.numberToColor(6).number == 1
  assert field.numberToColor(7).number == 0
  assert field.numberToColor(8).number == 1
  assert field.numberToColor(9).number == 1
  assert field.numberToColor(10).number == 0
  assert field.numberToColor(11).number == 1
  assert field.numberToColor(12).number == 0
  assert field.numberToColor(13).number == 1
  assert field.numberToColor(14).number == 0
  assert field.numberToColor(15).number == 1
  assert field.numberToColor(16).number == 0
  assert field.numberToColor(17).number == 0
  assert field.numberToColor(18).number == 1

def test_numberToColor_MaxElement_Odd():
  Config.Init(9)
  field = Field(1)
  assert field.numberToColor(1).number == 0
  assert field.numberToColor(2).number == 1
  assert field.numberToColor(3).number == 0
  assert field.numberToColor(4).number == 1
  assert field.numberToColor(5).number == 0
  assert field.numberToColor(6).number == 1
  assert field.numberToColor(7).number == 0
  assert field.numberToColor(8).number == 1
  assert field.numberToColor(9).number == 0

  assert field.numberToColor(10).number == 1
  assert field.numberToColor(11).number == 0
  assert field.numberToColor(12).number == 1
  assert field.numberToColor(13).number == 0
  assert field.numberToColor(14).number == 1
  assert field.numberToColor(15).number == 0
  assert field.numberToColor(16).number == 1
  assert field.numberToColor(17).number == 0
  assert field.numberToColor(18).number == 1

def test_getLastElement():
  Config.Init()
  field = Field(1)
  assert field.getLastElement() == 64

  Config.Init(9)
  field = Field(1)
  assert field.getLastElement() == 81
  
def test_getFirstElement():
  Config.Init()
  field = Field(1)
  assert field.getFirstElement() == 1

def test_isFilednumberInRange():
  Config.Init()
  field = Field(0)
  assert field.getFirstElement() == 1
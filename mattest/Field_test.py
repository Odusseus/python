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

def test_isFilednumberInRange_Return_False_When_Fieldnumber_Small_Than_First_Element():
  Config.Init()
  field = Field(0)
  assert field.isFilednumberInRange(0) == False

def test_isFilednumberInRange_Return_False_When_Fieldnumber_Tall_Than_Last_Element():
  Config.Init(5)
  field = Field(0)
  assert field.isFilednumberInRange(30) == False

def test_isFilednumberInRange_Return_True_When_Fieldnumber_Is_In_The_Range():
  Config.Init(5)
  field = Field(0)
  assert field.isFilednumberInRange(5) == True

def test_getFieldnumberUp():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberUp(5)[0] == True
  assert field.getFieldnumberUp(5)[1] == 8

  assert field.getFieldnumberUp(8)[0] == False
  assert field.getFieldnumberUp(8)[1] == None

def test_getFieldnumberUpRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberUpRight(5)[0] == True
  assert field.getFieldnumberUpRight(5)[1] == 9
  
  assert field.getFieldnumberUpRight(8)[0] == False
  assert field.getFieldnumberUpRight(8)[1] == None

def test_getFieldnumberUpLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberUpLeft(5)[0] == True
  assert field.getFieldnumberUpLeft(5)[1] == 7
  
  assert field.getFieldnumberUpLeft(8)[0] == False
  assert field.getFieldnumberUpLeft(8)[1] == None

def test_getFieldnumberDown():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberDown(5)[0] == True
  assert field.getFieldnumberDown(5)[1] == 2

  assert field.getFieldnumberDown(2)[0] == False
  assert field.getFieldnumberDown(2)[1] == None

def test_getFieldnumberDownRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberDownRight(5)[0] == True
  assert field.getFieldnumberDownRight(5)[1] == 3
  
  assert field.getFieldnumberDownRight(2)[0] == False
  assert field.getFieldnumberDownRight(2)[1] == None

def test_getFieldnumberdownLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberDownLeft(5)[0] == True
  assert field.getFieldnumberDownLeft(5)[1] == 1
  
  assert field.getFieldnumberDownLeft(2)[0] == False
  assert field.getFieldnumberDownLeft(2)[1] == None

def test_getFieldnumberLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberLeft(5)[0] == True
  assert field.getFieldnumberLeft(5)[1] == 4
  
  assert field.getFieldnumberLeft(4)[0] == False
  assert field.getFieldnumberLeft(4)[1] == None

def test_getFieldnumberRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldnumberRight(5)[0] == True
  assert field.getFieldnumberRight(5)[1] == 6
  
  assert field.getFieldnumberRight(6)[0] == False
  assert field.getFieldnumberRight(6)[1] == None




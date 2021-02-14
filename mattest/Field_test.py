import Config
import Constant
from Field import Field   # The code to test
from Piece import Piece

def test_Field_Black_Oddline():
  Config.Init()
  field = Field(1)

  assert field.color.id == Constant.BLACK
  assert field.color.name == Constant.BLACKNAME

def test_Field_Black_evenline():
  Config.Init()
  field = Field(10)

  assert field.color.id == Constant.BLACK
  assert field.color.name == Constant.BLACKNAME

def test_Field_White_oddline():
  Config.Init()
  field = Field(2)

  assert field.color.id == Constant.WHITE
  assert field.color.name == Constant.WHITENAME

def test_Field_White_evenline():
  Config.Init()
  field = Field(9)

  assert field.color.id == Constant.WHITE
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


def test_idToColor():
  Config.Init()
  field = Field(1)
  assert field.idToColor(1).id == 0
  assert field.idToColor(2).id == 1
  assert field.idToColor(3).id == 0
  assert field.idToColor(4).id == 1
  assert field.idToColor(5).id == 0
  assert field.idToColor(6).id == 1
  assert field.idToColor(7).id == 0
  assert field.idToColor(8).id == 1
  assert field.idToColor(9).id == 1
  assert field.idToColor(10).id == 0
  assert field.idToColor(11).id == 1
  assert field.idToColor(12).id == 0
  assert field.idToColor(13).id == 1
  assert field.idToColor(14).id == 0
  assert field.idToColor(15).id == 1
  assert field.idToColor(16).id == 0
  assert field.idToColor(17).id == 0
  assert field.idToColor(18).id == 1

def test_idToColor_MaxElement_Odd():
  Config.Init(9)
  field = Field(1)
  assert field.idToColor(1).id == 0
  assert field.idToColor(2).id == 1
  assert field.idToColor(3).id == 0
  assert field.idToColor(4).id == 1
  assert field.idToColor(5).id == 0
  assert field.idToColor(6).id == 1
  assert field.idToColor(7).id == 0
  assert field.idToColor(8).id == 1
  assert field.idToColor(9).id == 0

  assert field.idToColor(10).id == 1
  assert field.idToColor(11).id == 0
  assert field.idToColor(12).id == 1
  assert field.idToColor(13).id == 0
  assert field.idToColor(14).id == 1
  assert field.idToColor(15).id == 0
  assert field.idToColor(16).id == 1
  assert field.idToColor(17).id == 0
  assert field.idToColor(18).id == 1

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

def test_isFieldIdInRange_Return_False_When_FieldId_Small_Than_First_Element():
  Config.Init()
  field = Field(0)
  assert field.isFieldIdInRange(0) == False

def test_isFieldIdInRange_Return_False_When_FieldId_Tall_Than_Last_Element():
  Config.Init(5)
  field = Field(0)
  assert field.isFieldIdInRange(30) == False

def test_isFieldIdInRange_Return_True_When_FieldId_Is_In_The_Range():
  Config.Init(5)
  field = Field(0)
  assert field.isFieldIdInRange(5) == True

def test_getFieldIdUp():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdUp(5)[0] == True
  assert field.getFieldIdUp(5)[1] == 8

  assert field.getFieldIdUp(8)[0] == False
  assert field.getFieldIdUp(8)[1] == None

def test_getFieldIdUpRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdUpRight(5)[0] == True
  assert field.getFieldIdUpRight(5)[1] == 9
  
  assert field.getFieldIdUpRight(8)[0] == False
  assert field.getFieldIdUpRight(8)[1] == None

def test_getFieldIdUpLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdUpLeft(5)[0] == True
  assert field.getFieldIdUpLeft(5)[1] == 7
  
  assert field.getFieldIdUpLeft(8)[0] == False
  assert field.getFieldIdUpLeft(8)[1] == None

def test_getFieldIdDown():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdDown(5)[0] == True
  assert field.getFieldIdDown(5)[1] == 2

  assert field.getFieldIdDown(2)[0] == False
  assert field.getFieldIdDown(2)[1] == None

def test_getFieldIdDownRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdDownRight(5)[0] == True
  assert field.getFieldIdDownRight(5)[1] == 3
  
  assert field.getFieldIdDownRight(2)[0] == False
  assert field.getFieldIdDownRight(2)[1] == None

def test_getFieldIddownLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdDownLeft(5)[0] == True
  assert field.getFieldIdDownLeft(5)[1] == 1
  
  assert field.getFieldIdDownLeft(2)[0] == False
  assert field.getFieldIdDownLeft(2)[1] == None

def test_getFieldIdLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdLeft(5)[0] == True
  assert field.getFieldIdLeft(5)[1] == 4
  
  assert field.getFieldIdLeft(4)[0] == False
  assert field.getFieldIdLeft(4)[1] == None

def test_getFieldIdRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdRight(5)[0] == True
  assert field.getFieldIdRight(5)[1] == 6
  
  assert field.getFieldIdRight(6)[0] == False
  assert field.getFieldIdRight(6)[1] == None




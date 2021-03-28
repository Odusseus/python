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
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  
  # Act
  field.setPiece(piece)

  assert field.piece.name == Constant.KING

def test_removePiece():
  # Arrange
  Config.Init()
  field = Field(1)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
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
  assert field.getFieldIdUp(5).isSet == True
  assert field.getFieldIdUp(5).id == 8

  assert field.getFieldIdUp(8).isSet == False
  assert field.getFieldIdUp(8).id == None

def test_getFieldIdUpRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdUpRight(5).isSet == True
  assert field.getFieldIdUpRight(5).id == 9
  
  assert field.getFieldIdUpRight(8).isSet == False
  assert field.getFieldIdUpRight(8).id == None

def test_getFieldIdUpLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdUpLeft(5).isSet == True
  assert field.getFieldIdUpLeft(5).id == 7
  
  assert field.getFieldIdUpLeft(8).isSet == False
  assert field.getFieldIdUpLeft(8).id == None

def test_getFieldIdDown():
  Config.Init(3)
  field = Field(0)

  assert field.getFieldIdDown(5).isSet == True
  assert field.getFieldIdDown(5).id == 2

  assert field.getFieldIdDown(2).isSet == False
  assert field.getFieldIdDown(2).id == None

def test_getFieldIdDownRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdDownRight(5).isSet == True
  assert field.getFieldIdDownRight(5).id == 3
  
  assert field.getFieldIdDownRight(2).isSet == False
  assert field.getFieldIdDownRight(2).id == None

def test_getFieldIddownLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdDownLeft(5).isSet == True
  assert field.getFieldIdDownLeft(5).id == 1
  
  assert field.getFieldIdDownLeft(2).isSet == False
  assert field.getFieldIdDownLeft(2).id == None

def test_getFieldIdLeft():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdLeft(5).isSet == True
  assert field.getFieldIdLeft(5).id == 4
  
  assert field.getFieldIdLeft(4).isSet == False
  assert field.getFieldIdLeft(4).id == None

def test_getFieldIdRight():
  Config.Init(3)
  field = Field(0)
  assert field.getFieldIdRight(5).isSet == True
  assert field.getFieldIdRight(5).id == 6
  
  assert field.getFieldIdRight(6).isSet == False
  assert field.getFieldIdRight(6).id == None

def test_setIsTop_Board_is_1():
  Config.Init(1)
  field = Field(0)
  assert field.setIsTop(0) == False
  assert field.setIsTop(1) == True
  assert field.setIsTop(2) == False

def test_setIsTop_Board_is_2():
  Config.Init(2)
  field = Field(0)
  assert field.setIsTop(0) == False
  assert field.setIsTop(1) == False
  assert field.setIsTop(2) == False
  assert field.setIsTop(3) == True
  assert field.setIsTop(4) == True
  assert field.setIsTop(5) == False

def test_setIsTop_Board_is_3():
  Config.Init(3)
  field = Field(0)
  assert field.setIsTop(0) == False
  assert field.setIsTop(1) == False
  assert field.setIsTop(2) == False
  assert field.setIsTop(3) == False
  assert field.setIsTop(4) == False
  assert field.setIsTop(5) == False
  assert field.setIsTop(6) == False
  assert field.setIsTop(7) == True
  assert field.setIsTop(8) == True
  assert field.setIsTop(9) == True
  assert field.setIsTop(10) == False

def test_setIsBottom_Board_is_1():
  Config.Init(1)
  field = Field(0)
  assert field.setIsBottom(0) == False
  assert field.setIsBottom(1) == True
  assert field.setIsBottom(2) == False

def test_setIsBottom_Board_is_2():
  Config.Init(2)
  field = Field(0)
  assert field.setIsBottom(0) == False
  assert field.setIsBottom(1) == True
  assert field.setIsBottom(2) == True
  assert field.setIsBottom(3) == False
  assert field.setIsBottom(4) == False
  assert field.setIsBottom(5) == False

def test_setIsBottom_Board_is_3():
  Config.Init(3)
  field = Field(0)
  assert field.setIsBottom(0) == False
  assert field.setIsBottom(1) == True
  assert field.setIsBottom(2) == True
  assert field.setIsBottom(3) == True
  assert field.setIsBottom(4) == False
  assert field.setIsBottom(5) == False
  assert field.setIsBottom(6) == False
  assert field.setIsBottom(7) == False
  assert field.setIsBottom(8) == False
  assert field.setIsBottom(9) == False
  assert field.setIsBottom(10) == False

def test_setIsRight_Board_is_1():
  Config.Init(1)
  field = Field(0)
  assert field.setIsRight(0) == False
  assert field.setIsRight(1) == True
  assert field.setIsRight(2) == False

def test_setIsRight_Board_is_2():
  Config.Init(2)
  field = Field(0)
  assert field.setIsRight(0) == False
  assert field.setIsRight(1) == False
  assert field.setIsRight(2) == True
  assert field.setIsRight(3) == False
  assert field.setIsRight(4) == True
  assert field.setIsRight(5) == False

def test_setIsRight_Board_is_3():
  Config.Init(3)
  field = Field(0)
  assert field.setIsRight(0) == False
  assert field.setIsRight(1) == False
  assert field.setIsRight(2) == False
  assert field.setIsRight(3) == True
  assert field.setIsRight(4) == False
  assert field.setIsRight(5) == False
  assert field.setIsRight(6) == True
  assert field.setIsRight(7) == False
  assert field.setIsRight(8) == False
  assert field.setIsRight(9) == True
  assert field.setIsRight(10) == False

def test_setIsLeft_Board_is_1():
  Config.Init(1)
  field = Field(0)
  assert field.setIsLeft(0) == False
  assert field.setIsLeft(1) == True
  assert field.setIsLeft(2) == False

def test_setIsLeft_Board_is_2():
  Config.Init(2)
  field = Field(0)
  assert field.setIsLeft(0) == False
  assert field.setIsLeft(1) == True
  assert field.setIsLeft(2) == False
  assert field.setIsLeft(3) == True
  assert field.setIsLeft(4) == False
  assert field.setIsLeft(5) == False

def test_setIsLeft_Board_is_3():
  Config.Init(3)
  field = Field(0)
  assert field.setIsLeft(0) == False
  assert field.setIsLeft(1) == True
  assert field.setIsLeft(2) == False
  assert field.setIsLeft(3) == False
  assert field.setIsLeft(4) == True
  assert field.setIsLeft(5) == False
  assert field.setIsLeft(6) == False
  assert field.setIsLeft(7) == True
  assert field.setIsLeft(8) == False
  assert field.setIsLeft(9) == False
  assert field.setIsLeft(10) == False


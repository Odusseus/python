import Config
import Constant
import sys
import pytest
from Piece import Piece

def test_Piece_return_a_Piece():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  assert piece.color.id == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

def test_Piece_with_fieldId_return_a_Piece_on_a_fied():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 1)
  assert piece.color.id == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

  assert piece.field.id == 1
  assert piece.field.color.name == Constant.BLACKNAME
  assert piece.field.columnName == 'a'
  assert piece.field.lineName == 1

def test_Piece_with_fieldname_return_a_Piece_on_a_fied():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE,'a1')
  assert piece.color.id == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

  assert piece.field.id == 1
  assert piece.field.color.name == Constant.BLACKNAME
  assert piece.field.columnName == 'a'
  assert piece.field.lineName == 1

def test_Piece_with_invalide_fieldname_Raise_A_Error():
  Config.Init(8)
  
  try:
    Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE,'i1')
    assert True == False
  except Exception as e:
    assert e.__doc__ == "Mapping key not found."
  assert True == True

def test_Piece_clone_Return_a_Clone():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
    result = piece.clone()
    assert result.name == piece.name
    assert result.value == piece.value
    assert result.field == piece.field #is None because is not set
    assert result.color.id == piece.color.id

    piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE,'a1')
    
    result = piece.clone()
    assert result.name == piece.name
    assert result.value == piece.value
    assert result.field.id == piece.field.id
    assert result.color.id == piece.color.id

def test_getFieldReach():
  maxElement = 3
  Config.Init(maxElement)
    
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  
  with pytest.raises(Exception):
    piece.getFieldReach(1)  

def test_getCurrentReachs():
  maxElement = 3
  Config.Init(maxElement)
    
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  
  result = piece.getCurrentReachs()

  assert len(result) == 0

def test_setValue_3():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  
    piece.setValue(3)

    assert piece.value == 3

def test_setValue_default_king():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE)
  
    piece.setValue()

    assert piece.value == Constant.KINGVALUE

def test_setValue_default_queen():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.QUEEN, Constant.QUEENSHORT, Constant.BLACK, Constant.QUEENBLACKCODE, Constant.QUEENVALUE)
  
    piece.setValue()

    assert piece.value == Constant.QUEENVALUE

def test_setValue_default_Bishop():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.BISHOP, Constant.BISHOPSHORT, Constant.BLACK, Constant.BISHOPBLACKCODE, Constant.BISHOPVALUE)
  
    piece.setValue()

    assert piece.value == Constant.BISHOPVALUE

def test_setValue_default_Knight():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.KNIGHT, Constant.KNIGHTSHORT, Constant.BLACK, Constant.KNIGHTBLACKCODE, Constant.KNIGHTVALUE)
  
    piece.setValue()

    assert piece.value == Constant.KNIGHTVALUE

def test_setValue_default_Rook():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.ROOK, Constant.ROOKSHORT, Constant.BLACK, Constant.ROOKBLACKCODE, Constant.ROOKVALUE)
  
    piece.setValue()

    assert piece.value == Constant.ROOKVALUE

def test_setValue_default_PAWN():
    maxElement = 3
    Config.Init(maxElement)
    
    piece = Piece(Constant.PAWN, Constant.PAWNSHORT, Constant.BLACK, Constant.PAWNBLACKCODE, Constant.PAWNVALUE)
  
    piece.setValue()

    assert piece.value == Constant.PAWNVALUE
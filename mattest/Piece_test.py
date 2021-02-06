import Config
import Constant
import sys
from Piece import Piece

def test_Piece_return_a_Piece():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE)
  assert piece.color.number == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

def test_Piece_with_fieldnumber_return_a_Piece_on_a_fied():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, 1)
  assert piece.color.number == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

  assert piece.field.number == 1
  assert piece.field.color.name == Constant.BLACKNAME
  assert piece.field.columnName == 'a'
  assert piece.field.lineName == 1

def test_Piece_with_fieldname_return_a_Piece_on_a_fied():
  Config.Init(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE,'a1')
  assert piece.color.number == Constant.BLACK
  assert piece.color.name == Constant.BLACKNAME

  assert piece.field.number == 1
  assert piece.field.color.name == Constant.BLACKNAME
  assert piece.field.columnName == 'a'
  assert piece.field.lineName == 1

def test_Piece_with_invalide_fieldname_Raise_A_Error():
  Config.Init(8)
  
  try:
    Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE,'i1')
    assert True == False
  except Exception as e:
    assert e.__doc__ == "Mapping key not found."
  assert True == True
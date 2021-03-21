from typing import AbstractSet
import Config
import Constant
from Color import Color
from Board import Board
from Piece import Piece
from King import King

Config.Init()

def test_Board_return_a_Board():
  result = Board()

  assert result.name == Constant.DEFAULT  
  assert len(result.fields) == 65


def test_getMaxField_return_MaxField():
  Config.Init(8)
  result = Board()
  assert result.getMaxField() == 64

  Config.Init(9)
  result2 = Board()
  assert result2.getMaxField() == 81  


def test_setPiece_Add_a_piece():
  Config.Init(8)
  board = Board()
  king = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 1)
  queen = Piece(Constant.QUEEN, Constant.QUEENSHORT, Constant.WHITE, Constant.QUEENBLACKCODE, Constant.QUEENVALUE, 2)
  board.setPiece(king)
  board.setPiece(queen)

  assert board.fields[1].piece.name == Constant.KING
  assert board.fields[2].piece.name == Constant.QUEEN

def test_cleanField():
  Config.Init(8)
  board = Board()
  king = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 1)
  board.setPiece(king)

  # Act
  board.cleanField(1)

  assert board.fields[1].piece == None

def test_deletePiece():
  Config.Init(8)
  board = Board()
  kingWhite = Piece(Constant.KING, Constant.KINGSHORT, Constant.WHITE, Constant.KINGWHITECODE, Constant.KINGVALUE, 1)
  kingBlack = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 2)
  board.setPiece(kingWhite)
  board.setPiece(kingBlack)

  # Act
  board.deletePiece(kingWhite)
  board.deletePiece(kingBlack)

  assert board.fields[1].piece == None
  whitePieces = [
                whitePiece for whitePiece in board.whitePieces if whitePiece.id != kingWhite.id]
  assert len(whitePieces) == 0
  blackPieces = [
                blackPiece for blackPiece in board.blackPieces if blackPiece.id != kingBlack.id]
  assert len(blackPieces) == 0

def test_getPieces():
  Config.Init(8)
  board = Board()
  kingWhite = Piece(Constant.KING, Constant.KINGSHORT, Constant.WHITE, Constant.KINGWHITECODE, Constant.KINGVALUE, 1)
  kingBlack = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 2)
  board.setPiece(kingWhite)
  board.setPiece(kingBlack)

  # Act
  blackPieces = board.getPieces(Constant.BLACK)
  whitePieces = board.getPieces(Constant.WHITE)

  assert blackPieces[0].id == kingBlack.id
  assert whitePieces[0].id == kingWhite.id

def test_getAllPieces():
  Config.Init(8)
  board = Board()
  kingWhite = Piece(Constant.KING, Constant.KINGSHORT, Constant.WHITE, Constant.KINGWHITECODE, Constant.KINGVALUE, 1)
  kingBlack = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 2)
  board.setPiece(kingWhite)
  board.setPiece(kingBlack)

  # Act
  pieces = board.getAllPieces()

  assert len(pieces) == 2

def test_getKing():
  Config.Init(8)
  board = Board()
  kingWhite = Piece(Constant.KING, Constant.KINGSHORT, Constant.WHITE, Constant.KINGWHITECODE, Constant.KINGVALUE, 1)
  kingBlack = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, Constant.KINGVALUE, 2)
  board.setPiece(kingWhite)
  board.setPiece(kingBlack)

  # Act
  blackKing = board.getKing(Constant.BLACK)
  whiteKing = board.getKing(Constant.WHITE)

  assert blackKing != None
  assert whiteKing != None

def test_clone():
  Config.Init(8)
  board = Board()
  kingWhite = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  kingBlack = King(Constant.BLACK, Constant.KINGBLACKCODE, 2)
  board.setPiece(kingWhite)
  board.setPiece(kingBlack)

  # Act
  cloneBoard = board.clone()

  whiteClonePieces = cloneBoard.getPieces(Constant.WHITE)
  blackClonePieces = cloneBoard.getPieces(Constant.BLACK)

  assert cloneBoard != None
  assert len(whiteClonePieces) == 1
  assert whiteClonePieces[0].id != kingWhite.id
  assert blackClonePieces[0].id != kingBlack.id

def test_evaluate_return_0_when_board_is_empty():
  Config.Init(8)
  board = Board()

  # Act
  board.evaluate()

  assert board.value == 0

def test_evaluate_return_4_when_a_white_king_is_on_the_board():
  Config.Init(8)
  board = Board()
  kingWhite = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  board.setPiece(kingWhite)

  # Act
  board.evaluate()

  assert board.value == 4

def test_evaluate_return_min_4_when_a_black_king_is_on_the_board():
  Config.Init(8)
  board = Board()
  kingBlack = King(Constant.BLACK, Constant.KINGWHITECODE, 1)
  board.setPiece(kingBlack)

  # Act
  board.evaluate()

  assert board.value == -4

def test_evaluate_return_min_0_when_both_kings_are_on_the_board():
  Config.Init(8)
  board = Board()
  kingBlack = King(Constant.BLACK, Constant.KINGBLACKCODE, 1)
  kingWhite = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  board.setPiece(kingBlack)
  board.setPiece(kingWhite)

  # Act
  board.evaluate()

  assert board.value == 0

def test_setFieldsValue():
    Config.Init(8)
    board = Board()

    board.setFieldsValue()
    
    assert board.fields[1].value == 2
    assert board.fields[2].value == 3
    assert board.fields[3].value == 4
    assert board.fields[4].value == 5 
    assert board.fields[5].value == 5
    assert board.fields[6].value == 4
    assert board.fields[7].value == 3
    assert board.fields[8].value == 2

    assert board.fields[9].value == 3
    assert board.fields[10].value == 4
    assert board.fields[11].value == 5
    assert board.fields[12].value == 6
    assert board.fields[13].value == 6
    assert board.fields[14].value == 5
    assert board.fields[15].value == 4
    assert board.fields[16].value == 3
    
    assert board.fields[17].value == 4
    assert board.fields[18].value == 5
    assert board.fields[19].value == 6
    assert board.fields[20].value == 7
    assert board.fields[21].value == 7
    assert board.fields[22].value == 6
    assert board.fields[23].value == 5
    assert board.fields[24].value == 4 
    
    assert board.fields[25].value == 5
    assert board.fields[26].value == 6
    assert board.fields[27].value == 7
    assert board.fields[28].value == 8
    assert board.fields[29].value == 8
    assert board.fields[30].value == 7
    assert board.fields[31].value == 6
    assert board.fields[32].value == 5

    assert board.fields[33].value == 5
    assert board.fields[34].value == 6
    assert board.fields[35].value == 7
    assert board.fields[36].value == 8
    assert board.fields[37].value == 8
    assert board.fields[38].value == 7
    assert board.fields[39].value == 6
    assert board.fields[40].value == 5

    assert board.fields[41].value == 4
    assert board.fields[42].value == 5
    assert board.fields[43].value == 6
    assert board.fields[44].value == 7 
    assert board.fields[45].value == 7
    assert board.fields[46].value == 6
    assert board.fields[47].value == 5
    assert board.fields[48].value == 4

    assert board.fields[49].value == 3
    assert board.fields[50].value == 4
    assert board.fields[51].value == 5
    assert board.fields[52].value == 6
    assert board.fields[53].value == 6
    assert board.fields[54].value == 5
    assert board.fields[55].value == 4
    assert board.fields[56].value == 3
    
    assert board.fields[57].value == 2
    assert board.fields[58].value == 3
    assert board.fields[59].value == 4
    assert board.fields[60].value == 5
    assert board.fields[61].value == 5
    assert board.fields[62].value == 4
    assert board.fields[63].value == 3
    assert board.fields[64].value == 2 
    




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







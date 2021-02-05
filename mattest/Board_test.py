import Constant
from Board import Board
from Piece import Piece
from Config import Config

config = Config()

def test_Board_return_a_Board():
  result = Board(config)

  assert result.name == Constant.DEFAULT  
  assert len(result.fields) == 65


def test_getMaxField_return_MaxField():
  result = Board(config  )
  assert result.getMaxField() == 64

  config9 = Config(9)
  result2 = Board(config9)
  assert result2.getMaxField() == 81  


def test_getMaxField_Add_a_piece():
  board = Board(config)
  piece = Piece(config, Constant.KING, Constant.KINGSHORT, Constant.BLACK, 1)
  board.addPiece(piece)

  assert board.fields[1].piece.name == Constant.KING  



import Config
import Constant
from Board import Board
from Piece import Piece

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


def test_getMaxField_Add_a_piece():
  Config.Init(8)
  board = Board()
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, Constant.KINGBLACKCODE, 1)
  board.setPiece(piece)

  assert board.fields[1].piece.name == Constant.KING  



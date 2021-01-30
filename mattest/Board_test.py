import Constant
from Board import Board
from Piece import Piece

def test_Board_return_a_Board():
  result = Board()

  assert result.name == Constant.DEFAULT  
  assert len(result.fields) == 65


def test_getMaxField_return_MaxField():
  result = Board(8)
  result2 = Board(9)

  assert result.getMaxField() == 64  
  assert result2.getMaxField() == 81  


def test_getMaxField_Add_a_piece():
  board = Board(8)
  piece = Piece(Constant.KING, Constant.KINGSHORT, Constant.BLACK, 1)
  board.addPiece(piece)

  assert board.fields[1].piece.name == Constant.KING  



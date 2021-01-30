import Constant
from Box import Box

def test_Box_return_a_Box():
  box = Box()

  result = box.getKingBlack()  
  assert result.name == Constant.KING
  assert result.color.name == Constant.BLACKNAME

  result = box.getKingWhite()
  assert result.name == Constant.KING
  assert result.color.name == Constant.WHITENAME

  result = box.getQueenBlack()  
  assert result.name == Constant.QUEEN
  assert result.color.name == Constant.BLACKNAME

  result = box.getQueenWhite()
  assert result.name == Constant.QUEEN
  assert result.color.name == Constant.WHITENAME

  result = box.getBishopBlack()  
  assert result.name == Constant.BISHOP
  assert result.color.name == Constant.BLACKNAME

  result = box.getBishopWhite()
  assert result.name == Constant.BISHOP
  assert result.color.name == Constant.WHITENAME

  result = box.getKnightBlack()  
  assert result.name == Constant.KNIGHT
  assert result.color.name == Constant.BLACKNAME

  result = box.getKnightWhite()
  assert result.name == Constant.KNIGHT
  assert result.color.name == Constant.WHITENAME

  result = box.getPawnBlack()  
  assert result.name == Constant.PAWN
  assert result.color.name == Constant.BLACKNAME

  result = box.getPawnWhite()
  assert result.name == Constant.PAWN
  assert result.color.name == Constant.WHITENAME

  result = box.getRookBlack()  
  assert result.name == Constant.ROOK
  assert result.color.name == Constant.BLACKNAME

  result = box.getRookWhite()
  assert result.name == Constant.ROOK
  assert result.color.name == Constant.WHITENAME


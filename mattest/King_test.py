import Config
import Constant
from King import King

def test_King_return_a_King():
  Config.Init(8)
  result = King(Constant.BLACK, Constant.KINGBLACKCODE)
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME

def test_King_with_field_return_a_King_on_a_Field():
  Config.Init(8)
  result = King(Constant.BLACK, Constant.KINGBLACKCODE, 1)
  assert result.color.id == Constant.BLACK
  assert result.color.name == Constant.BLACKNAME
  assert result.name == Constant.KING
  assert result.shortName == Constant.KINGSHORT
  assert result.field.id == 1
  assert result.field.color.name == Constant.BLACKNAME
  assert result.field.columnName == 'a'
  assert result.field.lineName == 1

def test_King_getFieldReach_on_5():
  Config.Init(3)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 5)
  result = king.getFieldReach(5)
  assert len(result) == 8
  assert 1 in result
  assert 2 in result
  assert 3 in result
  assert 4 in result
  assert 5 not in result
  assert 6 in result
  assert 7 in result
  assert 8 in result
  assert 9 in result

def test_King_getFieldReach_on_1():
  Config.Init(3)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  result = king.getFieldReach(1)
  assert len(result) == 3
  assert 4 in result
  assert 5 in result
  assert 2 in result
  
def test_King_getReatch_When_maxElement_Is_1():
  maxElement = 1
  Config.Init(maxElement)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  result = king.getReachs()
  assert len(result) == 0

def test_King_getReach_When_maxElement_Is_2():
  maxElement = 2
  Config.Init(maxElement)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  result = king.getAllReachs()
  assert len(result) == 5
  assert result[1][0] == 3
  assert result[1][1] == 4
  assert result[1][2] == 2

  assert result[2][0] == 4
  assert result[2][1] == 1
  assert result[2][2] == 3

  assert result[3][0] == 4
  assert result[3][1] == 2
  assert result[3][2] == 1
  
  assert result[4][0] == 2
  assert result[4][1] == 1
  assert result[4][2] == 3

def test_King_getReach_When_maxElement_Is_3():
  maxElement = 3
  Config.Init(maxElement)
  king = King(Constant.WHITE, Constant.KINGWHITECODE, 1)
  result = king.getAllReachs()
  assert len(result) == 10

  assert result[1][0] == 4
  assert result[1][1] == 5
  assert result[1][2] == 2

  assert result[2][0] == 5
  assert result[2][1] == 6
  assert result[2][2] == 3
  assert result[2][3] == 1
  assert result[2][4] == 4

  assert result[3][0] == 6
  assert result[3][1] == 2
  assert result[3][2] == 5

  assert result[4][0] == 7
  assert result[4][1] == 8
  assert result[4][2] == 5
  assert result[4][3] == 2
  assert result[4][4] == 1

  assert result[5][0] == 8
  assert result[5][1] == 9
  assert result[5][2] == 6
  assert result[5][3] == 3
  assert result[5][4] == 2
  assert result[5][5] == 1
  assert result[5][6] == 4
  assert result[5][7] == 7

  assert result[6][0] == 9
  assert result[6][1] == 3
  assert result[6][2] == 2
  assert result[6][3] == 5
  assert result[6][4] == 8

  assert result[7][0] == 8
  assert result[7][1] == 5
  assert result[7][2] == 4

  assert result[8][0] == 9
  assert result[8][1] == 6
  assert result[8][2] == 5
  assert result[8][3] == 4
  assert result[8][4] == 7

  assert result[9][0] == 6
  assert result[9][1] == 5
  assert result[9][2] == 8
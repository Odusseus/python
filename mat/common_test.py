import Common   # The code to test

def test_numberToColumnName():
  assert Common.numberToColumnName(1) == 'a'
  assert Common.numberToColumnName(2) == 'b'
  assert Common.numberToColumnName(3) == 'c'
  assert Common.numberToColumnName(4) == 'd'
  assert Common.numberToColumnName(5) == 'e'
  assert Common.numberToColumnName(6) == 'f'
  assert Common.numberToColumnName(7) == 'g'
  assert Common.numberToColumnName(8) == 'h'
  assert Common.numberToColumnName(9) == 'a'
  assert Common.numberToColumnName(10) == 'b'
  assert Common.numberToColumnName(11) == 'c'
  assert Common.numberToColumnName(12) == 'd'
  assert Common.numberToColumnName(13) == 'e'
  assert Common.numberToColumnName(14) == 'f'
  assert Common.numberToColumnName(15) == 'g'
  assert Common.numberToColumnName(16) == 'h'
  assert Common.numberToColumnName(17) == 'a'
  assert Common.numberToColumnName(18) == 'b'
  assert Common.numberToColumnName(19) == 'c'
  assert Common.numberToColumnName(20) == 'd'
  assert Common.numberToColumnName(21) == 'e'
  assert Common.numberToColumnName(22) == 'f'
  assert Common.numberToColumnName(23) == 'g'
  assert Common.numberToColumnName(24) == 'h'
  assert Common.numberToColumnName(25) == 'a'
  assert Common.numberToColumnName(26) == 'b'
  assert Common.numberToColumnName(27) == 'c'
  assert Common.numberToColumnName(28) == 'd'
  assert Common.numberToColumnName(29) == 'e'
  assert Common.numberToColumnName(30) == 'f'
  assert Common.numberToColumnName(31) == 'g'
  assert Common.numberToColumnName(32) == 'h'
  assert Common.numberToColumnName(33) == 'a'
  assert Common.numberToColumnName(34) == 'b'
  assert Common.numberToColumnName(35) == 'c'
  assert Common.numberToColumnName(36) == 'd'
  assert Common.numberToColumnName(37) == 'e'
  assert Common.numberToColumnName(38) == 'f'
  assert Common.numberToColumnName(39) == 'g'
  assert Common.numberToColumnName(40) == 'h'
  assert Common.numberToColumnName(41) == 'a'
  assert Common.numberToColumnName(42) == 'b'
  assert Common.numberToColumnName(43) == 'c'
  assert Common.numberToColumnName(44) == 'd'
  assert Common.numberToColumnName(45) == 'e'
  assert Common.numberToColumnName(46) == 'f'
  assert Common.numberToColumnName(47) == 'g'
  assert Common.numberToColumnName(48) == 'h'
  assert Common.numberToColumnName(49) == 'a'
  assert Common.numberToColumnName(50) == 'b'
  assert Common.numberToColumnName(51) == 'c'
  assert Common.numberToColumnName(52) == 'd'
  assert Common.numberToColumnName(53) == 'e'
  assert Common.numberToColumnName(54) == 'f'
  assert Common.numberToColumnName(55) == 'g'
  assert Common.numberToColumnName(56) == 'h'
  assert Common.numberToColumnName(57) == 'a'
  assert Common.numberToColumnName(58) == 'b'
  assert Common.numberToColumnName(59) == 'c'
  assert Common.numberToColumnName(60) == 'd'
  assert Common.numberToColumnName(61) == 'e'
  assert Common.numberToColumnName(62) == 'f'
  assert Common.numberToColumnName(63) == 'g'
  assert Common.numberToColumnName(64) == 'h'
  
def test_numberToLineNumber():
  x = Common.numberToLineNumber(1)
  assert Common.numberToLineNumber(1) == 1
  assert Common.numberToLineNumber(2) == 1 
  assert Common.numberToLineNumber(3) == 1 
  assert Common.numberToLineNumber(4) == 1 
  assert Common.numberToLineNumber(5) == 1 
  assert Common.numberToLineNumber(6) == 1 
  assert Common.numberToLineNumber(7) == 1 
  assert Common.numberToLineNumber(8) == 1 
  assert Common.numberToLineNumber(9) == 2 
  assert Common.numberToLineNumber(10) == 2
  assert Common.numberToLineNumber(11) == 2
  assert Common.numberToLineNumber(12) == 2
  assert Common.numberToLineNumber(13) == 2
  assert Common.numberToLineNumber(14) == 2
  assert Common.numberToLineNumber(15) == 2
  assert Common.numberToLineNumber(16) == 2
  assert Common.numberToLineNumber(17) == 3
  assert Common.numberToLineNumber(18) == 3
  assert Common.numberToLineNumber(19) == 3
  assert Common.numberToLineNumber(20) == 3
  assert Common.numberToLineNumber(21) == 3
  assert Common.numberToLineNumber(22) == 3
  assert Common.numberToLineNumber(23) == 3
  assert Common.numberToLineNumber(24) == 3
  assert Common.numberToLineNumber(25) == 4
  assert Common.numberToLineNumber(26) == 4
  assert Common.numberToLineNumber(27) == 4
  assert Common.numberToLineNumber(28) == 4
  assert Common.numberToLineNumber(29) == 4
  assert Common.numberToLineNumber(30) == 4
  assert Common.numberToLineNumber(31) == 4
  assert Common.numberToLineNumber(32) == 4
  assert Common.numberToLineNumber(33) == 5
  assert Common.numberToLineNumber(34) == 5
  assert Common.numberToLineNumber(35) == 5
  assert Common.numberToLineNumber(36) == 5
  assert Common.numberToLineNumber(37) == 5
  assert Common.numberToLineNumber(38) == 5
  assert Common.numberToLineNumber(39) == 5
  assert Common.numberToLineNumber(40) == 5
  assert Common.numberToLineNumber(41) == 6
  assert Common.numberToLineNumber(42) == 6
  assert Common.numberToLineNumber(43) == 6
  assert Common.numberToLineNumber(44) == 6
  assert Common.numberToLineNumber(45) == 6
  assert Common.numberToLineNumber(46) == 6
  assert Common.numberToLineNumber(47) == 6
  assert Common.numberToLineNumber(48) == 6
  assert Common.numberToLineNumber(49) == 7
  assert Common.numberToLineNumber(50) == 7
  assert Common.numberToLineNumber(51) == 7
  assert Common.numberToLineNumber(52) == 7
  assert Common.numberToLineNumber(53) == 7
  assert Common.numberToLineNumber(54) == 7
  assert Common.numberToLineNumber(55) == 7
  assert Common.numberToLineNumber(56) == 7
  assert Common.numberToLineNumber(57) == 8
  assert Common.numberToLineNumber(58) == 8
  assert Common.numberToLineNumber(59) == 8
  assert Common.numberToLineNumber(60) == 8
  assert Common.numberToLineNumber(61) == 8
  assert Common.numberToLineNumber(62) == 8
  assert Common.numberToLineNumber(63) == 8
  assert Common.numberToLineNumber(64) == 8
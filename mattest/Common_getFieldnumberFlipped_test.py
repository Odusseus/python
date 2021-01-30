import Common   # The code to test

def test_getFieldnumberFlipped_max_1():
  assert Common.getFieldnumberFlipped(1, 1, 1) == 1

def test_getFieldnumberFlipped_max_2():
  assert Common.getFieldnumberFlipped(1, 1, 2) == 2  
  assert Common.getFieldnumberFlipped(1, 2, 2) == 1
  assert Common.getFieldnumberFlipped(2, 1, 2) == 4
  assert Common.getFieldnumberFlipped(2, 2, 2) == 3

def test_getFieldnumberFlipped_max_3():
  assert Common.getFieldnumberFlipped(1, 1, 3) == 3  
  assert Common.getFieldnumberFlipped(1, 2, 3) == 2
  assert Common.getFieldnumberFlipped(1, 3, 3) == 1
  assert Common.getFieldnumberFlipped(2, 1, 3) == 6
  assert Common.getFieldnumberFlipped(2, 2, 3) == 5
  assert Common.getFieldnumberFlipped(2, 3, 3) == 4
  
def test_getFieldnumberFlipped_max_8():
  assert Common.getFieldnumberFlipped(1, 1, 8) == 8  
  assert Common.getFieldnumberFlipped(1, 2, 8) == 7
  assert Common.getFieldnumberFlipped(1, 3, 8) == 6
  assert Common.getFieldnumberFlipped(1, 4, 8) == 5
  assert Common.getFieldnumberFlipped(1, 5, 8) == 4
  assert Common.getFieldnumberFlipped(1, 6, 8) == 3
  assert Common.getFieldnumberFlipped(1, 7, 8) == 2
  assert Common.getFieldnumberFlipped(1, 8, 8) == 1

  assert Common.getFieldnumberFlipped(2, 1, 8) == 16
  assert Common.getFieldnumberFlipped(2, 2, 8) == 15
  assert Common.getFieldnumberFlipped(2, 3, 8) == 14
  assert Common.getFieldnumberFlipped(2, 4, 8) == 13
  assert Common.getFieldnumberFlipped(2, 5, 8) == 12
  assert Common.getFieldnumberFlipped(2, 6, 8) == 11
  assert Common.getFieldnumberFlipped(2, 7, 8) == 10
  assert Common.getFieldnumberFlipped(2, 8, 8) == 9

  assert Common.getFieldnumberFlipped(3, 1, 8) == 24
  assert Common.getFieldnumberFlipped(3, 2, 8) == 23
  assert Common.getFieldnumberFlipped(3, 3, 8) == 22
  assert Common.getFieldnumberFlipped(3, 4, 8) == 21
  assert Common.getFieldnumberFlipped(3, 5, 8) == 20
  assert Common.getFieldnumberFlipped(3, 6, 8) == 19
  assert Common.getFieldnumberFlipped(3, 7, 8) == 18
  assert Common.getFieldnumberFlipped(3, 8, 8) == 17

  assert Common.getFieldnumberFlipped(4, 1, 8) == 32
  assert Common.getFieldnumberFlipped(4, 2, 8) == 31
  assert Common.getFieldnumberFlipped(4, 3, 8) == 30
  assert Common.getFieldnumberFlipped(4, 4, 8) == 29
  assert Common.getFieldnumberFlipped(4, 5, 8) == 28
  assert Common.getFieldnumberFlipped(4, 6, 8) == 27
  assert Common.getFieldnumberFlipped(4, 7, 8) == 26
  assert Common.getFieldnumberFlipped(4, 8, 8) == 25

  assert Common.getFieldnumberFlipped(5, 1, 8) == 40
  assert Common.getFieldnumberFlipped(5, 2, 8) == 39
  assert Common.getFieldnumberFlipped(5, 3, 8) == 38
  assert Common.getFieldnumberFlipped(5, 4, 8) == 37
  assert Common.getFieldnumberFlipped(5, 5, 8) == 36
  assert Common.getFieldnumberFlipped(5, 6, 8) == 35
  assert Common.getFieldnumberFlipped(5, 7, 8) == 34
  assert Common.getFieldnumberFlipped(5, 8, 8) == 33

  assert Common.getFieldnumberFlipped(6, 1, 8) == 48
  assert Common.getFieldnumberFlipped(6, 2, 8) == 47
  assert Common.getFieldnumberFlipped(6, 3, 8) == 46
  assert Common.getFieldnumberFlipped(6, 4, 8) == 45
  assert Common.getFieldnumberFlipped(6, 5, 8) == 44
  assert Common.getFieldnumberFlipped(6, 6, 8) == 43
  assert Common.getFieldnumberFlipped(6, 7, 8) == 42
  assert Common.getFieldnumberFlipped(6, 8, 8) == 41

  assert Common.getFieldnumberFlipped(7, 1, 8) == 56
  assert Common.getFieldnumberFlipped(7, 2, 8) == 55
  assert Common.getFieldnumberFlipped(7, 3, 8) == 54
  assert Common.getFieldnumberFlipped(7, 4, 8) == 53
  assert Common.getFieldnumberFlipped(7, 5, 8) == 52
  assert Common.getFieldnumberFlipped(7, 6, 8) == 51
  assert Common.getFieldnumberFlipped(7, 7, 8) == 50
  assert Common.getFieldnumberFlipped(7, 8, 8) == 49

  assert Common.getFieldnumberFlipped(8, 1, 8) == 64
  assert Common.getFieldnumberFlipped(8, 2, 8) == 63
  assert Common.getFieldnumberFlipped(8, 3, 8) == 62
  assert Common.getFieldnumberFlipped(8, 4, 8) == 61
  assert Common.getFieldnumberFlipped(8, 5, 8) == 60
  assert Common.getFieldnumberFlipped(8, 6, 8) == 59
  assert Common.getFieldnumberFlipped(8, 7, 8) == 58
  assert Common.getFieldnumberFlipped(8, 8, 8) == 57
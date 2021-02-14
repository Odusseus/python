import Common   # The code to test

def test_getFieldIdFlipped_max_1():
  assert Common.getFieldIdFlipped(1, 1, 1) == 1

def test_getFieldIdFlipped_max_2():
  assert Common.getFieldIdFlipped(1, 1, 2) == 2  
  assert Common.getFieldIdFlipped(1, 2, 2) == 1
  assert Common.getFieldIdFlipped(2, 1, 2) == 4
  assert Common.getFieldIdFlipped(2, 2, 2) == 3

def test_getFieldIdFlipped_max_3():
  assert Common.getFieldIdFlipped(1, 1, 3) == 3  
  assert Common.getFieldIdFlipped(1, 2, 3) == 2
  assert Common.getFieldIdFlipped(1, 3, 3) == 1
  assert Common.getFieldIdFlipped(2, 1, 3) == 6
  assert Common.getFieldIdFlipped(2, 2, 3) == 5
  assert Common.getFieldIdFlipped(2, 3, 3) == 4
  
def test_getFieldIdFlipped_max_8():
  assert Common.getFieldIdFlipped(1, 1, 8) == 8  
  assert Common.getFieldIdFlipped(1, 2, 8) == 7
  assert Common.getFieldIdFlipped(1, 3, 8) == 6
  assert Common.getFieldIdFlipped(1, 4, 8) == 5
  assert Common.getFieldIdFlipped(1, 5, 8) == 4
  assert Common.getFieldIdFlipped(1, 6, 8) == 3
  assert Common.getFieldIdFlipped(1, 7, 8) == 2
  assert Common.getFieldIdFlipped(1, 8, 8) == 1

  assert Common.getFieldIdFlipped(2, 1, 8) == 16
  assert Common.getFieldIdFlipped(2, 2, 8) == 15
  assert Common.getFieldIdFlipped(2, 3, 8) == 14
  assert Common.getFieldIdFlipped(2, 4, 8) == 13
  assert Common.getFieldIdFlipped(2, 5, 8) == 12
  assert Common.getFieldIdFlipped(2, 6, 8) == 11
  assert Common.getFieldIdFlipped(2, 7, 8) == 10
  assert Common.getFieldIdFlipped(2, 8, 8) == 9

  assert Common.getFieldIdFlipped(3, 1, 8) == 24
  assert Common.getFieldIdFlipped(3, 2, 8) == 23
  assert Common.getFieldIdFlipped(3, 3, 8) == 22
  assert Common.getFieldIdFlipped(3, 4, 8) == 21
  assert Common.getFieldIdFlipped(3, 5, 8) == 20
  assert Common.getFieldIdFlipped(3, 6, 8) == 19
  assert Common.getFieldIdFlipped(3, 7, 8) == 18
  assert Common.getFieldIdFlipped(3, 8, 8) == 17

  assert Common.getFieldIdFlipped(4, 1, 8) == 32
  assert Common.getFieldIdFlipped(4, 2, 8) == 31
  assert Common.getFieldIdFlipped(4, 3, 8) == 30
  assert Common.getFieldIdFlipped(4, 4, 8) == 29
  assert Common.getFieldIdFlipped(4, 5, 8) == 28
  assert Common.getFieldIdFlipped(4, 6, 8) == 27
  assert Common.getFieldIdFlipped(4, 7, 8) == 26
  assert Common.getFieldIdFlipped(4, 8, 8) == 25

  assert Common.getFieldIdFlipped(5, 1, 8) == 40
  assert Common.getFieldIdFlipped(5, 2, 8) == 39
  assert Common.getFieldIdFlipped(5, 3, 8) == 38
  assert Common.getFieldIdFlipped(5, 4, 8) == 37
  assert Common.getFieldIdFlipped(5, 5, 8) == 36
  assert Common.getFieldIdFlipped(5, 6, 8) == 35
  assert Common.getFieldIdFlipped(5, 7, 8) == 34
  assert Common.getFieldIdFlipped(5, 8, 8) == 33

  assert Common.getFieldIdFlipped(6, 1, 8) == 48
  assert Common.getFieldIdFlipped(6, 2, 8) == 47
  assert Common.getFieldIdFlipped(6, 3, 8) == 46
  assert Common.getFieldIdFlipped(6, 4, 8) == 45
  assert Common.getFieldIdFlipped(6, 5, 8) == 44
  assert Common.getFieldIdFlipped(6, 6, 8) == 43
  assert Common.getFieldIdFlipped(6, 7, 8) == 42
  assert Common.getFieldIdFlipped(6, 8, 8) == 41

  assert Common.getFieldIdFlipped(7, 1, 8) == 56
  assert Common.getFieldIdFlipped(7, 2, 8) == 55
  assert Common.getFieldIdFlipped(7, 3, 8) == 54
  assert Common.getFieldIdFlipped(7, 4, 8) == 53
  assert Common.getFieldIdFlipped(7, 5, 8) == 52
  assert Common.getFieldIdFlipped(7, 6, 8) == 51
  assert Common.getFieldIdFlipped(7, 7, 8) == 50
  assert Common.getFieldIdFlipped(7, 8, 8) == 49

  assert Common.getFieldIdFlipped(8, 1, 8) == 64
  assert Common.getFieldIdFlipped(8, 2, 8) == 63
  assert Common.getFieldIdFlipped(8, 3, 8) == 62
  assert Common.getFieldIdFlipped(8, 4, 8) == 61
  assert Common.getFieldIdFlipped(8, 5, 8) == 60
  assert Common.getFieldIdFlipped(8, 6, 8) == 59
  assert Common.getFieldIdFlipped(8, 7, 8) == 58
  assert Common.getFieldIdFlipped(8, 8, 8) == 57
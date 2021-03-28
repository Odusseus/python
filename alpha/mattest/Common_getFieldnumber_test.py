import Common   # The code to test

def test_getFieldId_max_1():
  assert Common.getFieldId(1, 1, 1) == 1

def test_getFieldId_max_2():
  assert Common.getFieldId(1, 1, 2) == 1  
  assert Common.getFieldId(1, 2, 2) == 2
  assert Common.getFieldId(2, 1, 2) == 3
  assert Common.getFieldId(2, 2, 2) == 4

def test_getFieldId_max_3():
  assert Common.getFieldId(1, 1, 3) == 1  
  assert Common.getFieldId(1, 2, 3) == 2
  assert Common.getFieldId(1, 3, 3) == 3
  assert Common.getFieldId(2, 1, 3) == 4
  assert Common.getFieldId(2, 2, 3) == 5
  assert Common.getFieldId(2, 3, 3) == 6
  
def test_getFieldId_max_8():
  assert Common.getFieldId(1, 1, 8) == 1
  assert Common.getFieldId(1, 2, 8) == 2
  assert Common.getFieldId(1, 3, 8) == 3
  assert Common.getFieldId(1, 4, 8) == 4
  assert Common.getFieldId(1, 5, 8) == 5
  assert Common.getFieldId(1, 6, 8) == 6
  assert Common.getFieldId(1, 7, 8) == 7
  assert Common.getFieldId(1, 8, 8) == 8

  assert Common.getFieldId(2, 1, 8) == 9
  assert Common.getFieldId(2, 2, 8) == 10
  assert Common.getFieldId(2, 3, 8) == 11
  assert Common.getFieldId(2, 4, 8) == 12
  assert Common.getFieldId(2, 5, 8) == 13
  assert Common.getFieldId(2, 6, 8) == 14
  assert Common.getFieldId(2, 7, 8) == 15
  assert Common.getFieldId(2, 8, 8) == 16

  assert Common.getFieldId(3, 1, 8) == 17
  assert Common.getFieldId(3, 2, 8) == 18
  assert Common.getFieldId(3, 3, 8) == 19
  assert Common.getFieldId(3, 4, 8) == 20
  assert Common.getFieldId(3, 5, 8) == 21
  assert Common.getFieldId(3, 6, 8) == 22
  assert Common.getFieldId(3, 7, 8) == 23
  assert Common.getFieldId(3, 8, 8) == 24

  assert Common.getFieldId(4, 1, 8) == 25
  assert Common.getFieldId(4, 2, 8) == 26
  assert Common.getFieldId(4, 3, 8) == 27
  assert Common.getFieldId(4, 4, 8) == 28
  assert Common.getFieldId(4, 5, 8) == 29
  assert Common.getFieldId(4, 6, 8) == 30
  assert Common.getFieldId(4, 7, 8) == 31
  assert Common.getFieldId(4, 8, 8) == 32

  assert Common.getFieldId(5, 1, 8) == 33
  assert Common.getFieldId(5, 2, 8) == 34
  assert Common.getFieldId(5, 3, 8) == 35
  assert Common.getFieldId(5, 4, 8) == 36
  assert Common.getFieldId(5, 5, 8) == 37
  assert Common.getFieldId(5, 6, 8) == 38
  assert Common.getFieldId(5, 7, 8) == 39
  assert Common.getFieldId(5, 8, 8) == 40

  assert Common.getFieldId(6, 1, 8) == 41
  assert Common.getFieldId(6, 2, 8) == 42
  assert Common.getFieldId(6, 3, 8) == 43
  assert Common.getFieldId(6, 4, 8) == 44
  assert Common.getFieldId(6, 5, 8) == 45
  assert Common.getFieldId(6, 6, 8) == 46
  assert Common.getFieldId(6, 7, 8) == 47
  assert Common.getFieldId(6, 8, 8) == 48

  assert Common.getFieldId(7, 1, 8) == 49
  assert Common.getFieldId(7, 2, 8) == 50
  assert Common.getFieldId(7, 3, 8) == 51
  assert Common.getFieldId(7, 4, 8) == 52
  assert Common.getFieldId(7, 5, 8) == 53
  assert Common.getFieldId(7, 6, 8) == 54
  assert Common.getFieldId(7, 7, 8) == 55
  assert Common.getFieldId(7, 8, 8) == 56

  assert Common.getFieldId(8, 1, 8) == 57
  assert Common.getFieldId(8, 2, 8) == 58
  assert Common.getFieldId(8, 3, 8) == 59
  assert Common.getFieldId(8, 4, 8) == 60
  assert Common.getFieldId(8, 5, 8) == 61
  assert Common.getFieldId(8, 6, 8) == 62
  assert Common.getFieldId(8, 7, 8) == 63
  assert Common.getFieldId(8, 8, 8) == 64
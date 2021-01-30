import Common   # The code to test

def test_getFieldnumber_max_1():
  assert Common.getFieldnumber(1, 1, 1) == 1

def test_getFieldnumber_max_2():
  assert Common.getFieldnumber(1, 1, 2) == 1  
  assert Common.getFieldnumber(1, 2, 2) == 2
  assert Common.getFieldnumber(2, 1, 2) == 3
  assert Common.getFieldnumber(2, 2, 2) == 4

def test_getFieldnumber_max_3():
  assert Common.getFieldnumber(1, 1, 3) == 1  
  assert Common.getFieldnumber(1, 2, 3) == 2
  assert Common.getFieldnumber(1, 3, 3) == 3
  assert Common.getFieldnumber(2, 1, 3) == 4
  assert Common.getFieldnumber(2, 2, 3) == 5
  assert Common.getFieldnumber(2, 3, 3) == 6
  
def test_getFieldnumber_max_8():
  assert Common.getFieldnumber(1, 1, 8) == 1
  assert Common.getFieldnumber(1, 2, 8) == 2
  assert Common.getFieldnumber(1, 3, 8) == 3
  assert Common.getFieldnumber(1, 4, 8) == 4
  assert Common.getFieldnumber(1, 5, 8) == 5
  assert Common.getFieldnumber(1, 6, 8) == 6
  assert Common.getFieldnumber(1, 7, 8) == 7
  assert Common.getFieldnumber(1, 8, 8) == 8

  assert Common.getFieldnumber(2, 1, 8) == 9
  assert Common.getFieldnumber(2, 2, 8) == 10
  assert Common.getFieldnumber(2, 3, 8) == 11
  assert Common.getFieldnumber(2, 4, 8) == 12
  assert Common.getFieldnumber(2, 5, 8) == 13
  assert Common.getFieldnumber(2, 6, 8) == 14
  assert Common.getFieldnumber(2, 7, 8) == 15
  assert Common.getFieldnumber(2, 8, 8) == 16

  assert Common.getFieldnumber(3, 1, 8) == 17
  assert Common.getFieldnumber(3, 2, 8) == 18
  assert Common.getFieldnumber(3, 3, 8) == 19
  assert Common.getFieldnumber(3, 4, 8) == 20
  assert Common.getFieldnumber(3, 5, 8) == 21
  assert Common.getFieldnumber(3, 6, 8) == 22
  assert Common.getFieldnumber(3, 7, 8) == 23
  assert Common.getFieldnumber(3, 8, 8) == 24

  assert Common.getFieldnumber(4, 1, 8) == 25
  assert Common.getFieldnumber(4, 2, 8) == 26
  assert Common.getFieldnumber(4, 3, 8) == 27
  assert Common.getFieldnumber(4, 4, 8) == 28
  assert Common.getFieldnumber(4, 5, 8) == 29
  assert Common.getFieldnumber(4, 6, 8) == 30
  assert Common.getFieldnumber(4, 7, 8) == 31
  assert Common.getFieldnumber(4, 8, 8) == 32

  assert Common.getFieldnumber(5, 1, 8) == 33
  assert Common.getFieldnumber(5, 2, 8) == 34
  assert Common.getFieldnumber(5, 3, 8) == 35
  assert Common.getFieldnumber(5, 4, 8) == 36
  assert Common.getFieldnumber(5, 5, 8) == 37
  assert Common.getFieldnumber(5, 6, 8) == 38
  assert Common.getFieldnumber(5, 7, 8) == 39
  assert Common.getFieldnumber(5, 8, 8) == 40

  assert Common.getFieldnumber(6, 1, 8) == 41
  assert Common.getFieldnumber(6, 2, 8) == 42
  assert Common.getFieldnumber(6, 3, 8) == 43
  assert Common.getFieldnumber(6, 4, 8) == 44
  assert Common.getFieldnumber(6, 5, 8) == 45
  assert Common.getFieldnumber(6, 6, 8) == 46
  assert Common.getFieldnumber(6, 7, 8) == 47
  assert Common.getFieldnumber(6, 8, 8) == 48

  assert Common.getFieldnumber(7, 1, 8) == 49
  assert Common.getFieldnumber(7, 2, 8) == 50
  assert Common.getFieldnumber(7, 3, 8) == 51
  assert Common.getFieldnumber(7, 4, 8) == 52
  assert Common.getFieldnumber(7, 5, 8) == 53
  assert Common.getFieldnumber(7, 6, 8) == 54
  assert Common.getFieldnumber(7, 7, 8) == 55
  assert Common.getFieldnumber(7, 8, 8) == 56

  assert Common.getFieldnumber(8, 1, 8) == 57
  assert Common.getFieldnumber(8, 2, 8) == 58
  assert Common.getFieldnumber(8, 3, 8) == 59
  assert Common.getFieldnumber(8, 4, 8) == 60
  assert Common.getFieldnumber(8, 5, 8) == 61
  assert Common.getFieldnumber(8, 6, 8) == 62
  assert Common.getFieldnumber(8, 7, 8) == 63
  assert Common.getFieldnumber(8, 8, 8) == 64
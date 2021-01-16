from Field import Field   # The code to test

def test_numberToColor():
  field = Field(1)
  assert field.numberToColor(1).number == 0
  assert field.numberToColor(2).number == 1
  assert field.numberToColor(3).number == 0
  assert field.numberToColor(4).number == 1
  assert field.numberToColor(5).number == 0
  assert field.numberToColor(6).number == 1
  assert field.numberToColor(7).number == 0
  assert field.numberToColor(8).number == 1
  assert field.numberToColor(9).number == 1
  assert field.numberToColor(1, 9).number == 0
  assert field.numberToColor(9, 9).number == 0
  assert field.numberToColor(10, 9).number == 0
  assert field.numberToColor(10).number == 0
  assert field.numberToColor(11).number == 1
  assert field.numberToColor(12).number == 0
  assert field.numberToColor(13).number == 1
  assert field.numberToColor(14).number == 0
  assert field.numberToColor(15).number == 1
  assert field.numberToColor(16).number == 0
  assert field.numberToColor(17).number == 0
  assert field.numberToColor(18).number == 1
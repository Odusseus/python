import math

def numberToColumnName(number):
 switcher = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        0: "h"
    }
 return switcher.get(number % 8,'?')

def numberToLineNumber(number):
  line = math.ceil(number / 8)
  return line
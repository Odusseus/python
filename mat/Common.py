import math

def numberToColumnName(number, max): 
  ALPHABET_BASE = 96
  MAX_LETTER = 26

  cycle = math.ceil(number / max)
  numberB = number - (max * (cycle - 1))
  cycle2 = math.ceil(numberB / MAX_LETTER)
  if numberB > MAX_LETTER:
    numberB = numberB - (MAX_LETTER * (cycle2 -1 ))
  letterNumber = numberB + ALPHABET_BASE

  letter = chr(letterNumber)
  letters = repeatToLength(letter, cycle2)
  return letters

def numberToLineNumber(number, max):
  line = math.ceil(number / max)
  return line

def repeatToLength(string_to_expand, length):
  return (string_to_expand * (int)((length/len(string_to_expand))+1))[:length]

def getFieldnumber(line, column, max):
  return ((line - 1) * max) + column

def getFieldnumberFlipped(line, column, max):  
  return ((line - 1) * max) + (max - column + 1)

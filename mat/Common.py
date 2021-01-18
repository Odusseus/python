import math

def numberToColumnName(number, max): 
  ALPHABET_BASE = 96
  MAX_LETTER = 26
  cycle = math.ceil(max / MAX_LETTER)

  letterNumber = number % max
  if letterNumber == 0:
    letterNumber = letterNumber + max + ALPHABET_BASE
  else:
    letterNumber = letterNumber + ALPHABET_BASE
 
  letter = chr(letterNumber)
  letters = repeatToLength(letter, cycle)
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

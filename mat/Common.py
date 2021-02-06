import math

def numberToColumnName(number, max): 
  ALPHABET_BASE = 96
  MAX_LETTER = 26

  cycle = math.floor(number / max)
  if number % max == 0:
    cycle = cycle - 1
  numberB = number - (max * cycle)

  if numberB > MAX_LETTER:
    numberB = numberB - MAX_LETTER

  letterNumber = numberB + ALPHABET_BASE
 
  letter = chr(letterNumber)
  return letter
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

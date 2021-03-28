import math

def idToColumnName(id, max): 
  ALPHABET_BASE = 96
  MAX_LETTER = 26

  cycle = math.ceil(id / max)
  idB = id - (max * (cycle - 1))
  cycle2 = math.ceil(idB / MAX_LETTER)
  if idB > MAX_LETTER:
    idB = idB - (MAX_LETTER * (cycle2 -1 ))
  letterNumber = idB + ALPHABET_BASE

  letter = chr(letterNumber)
  letters = repeatToLength(letter, cycle2)
  return letters

def idToLineNumber(id, max):
  line = math.ceil(id / max)
  return line

def repeatToLength(string_to_expand, length):
  return (string_to_expand * (int)((length/len(string_to_expand))+1))[:length]

def getFieldId(line, column, max):
  return ((line - 1) * max) + column

def getFieldIdFlipped(line, column, max):  
  return ((line - 1) * max) + (max - column + 1)

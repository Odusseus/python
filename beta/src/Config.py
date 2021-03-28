import Constant
import Config

def Init(maxElementIn = Constant.MAX_ELEMENT, randomIn = False):
  global maxElement
  maxElement = maxElementIn
  
  global minElement
  minElement = 1

  global maxFieldId
  maxFieldId = maxElementIn * maxElementIn
  
  global minFieldId
  minFieldId = minElement
  
  global random
  random = randomIn

  global maxPiece
  maxPiece = 0

def nextPiece():
  Config.maxPiece += 1
  return maxPiece
import Constant

def Init(maxElementIn = Constant.MAX_ELEMENT, minElementIn = 1, randomIn = False):
  global maxElement
  maxElement = maxElementIn
  
  global minElement
  minElement = minElementIn

  global maxFieldId
  maxFieldId = maxElementIn * maxElementIn
  
  global minFieldId
  minFieldId = minElementIn
  
  global random
  random = randomIn
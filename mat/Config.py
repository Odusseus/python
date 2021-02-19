import Constant

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
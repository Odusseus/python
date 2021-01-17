import pathlib
import os
import Constant
import Common
from Board import Board
#import dominate
from dominate.tags import html, body, table, tbody, tr, th, td

board = Board('First', Constant.MAX_ELEMENT)
print('Allo, allo my name is ' + board.name)
print('I have ' + str(board.maxField()) + ' fields')

for i in range(len(board.fields)):
 print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())


page = html()
body = page.add(body())
table = body.add(table())
tbody = table.add(tbody())
maxLineBoard = Constant.MAX_ELEMENT + 1
maxLine = maxLineBoard + 1
maxField = Constant.MAX_ELEMENT * Constant.MAX_ELEMENT
currentField = 0
for i in range(1, maxLine):
  print(i)
  if (i < maxLineBoard):    
    tr1 = tbody.add(tr())
    line = Constant.MAX_ELEMENT + 1 - i
    for j in range(1, Constant.MAX_ELEMENT + 1):      
      if j == 1: 
        tr1.add(th(line))
      fieldnumber = Common.getFieldnumber(line, j, Constant.MAX_ELEMENT)
      print(fieldnumber)
      tr1.add(td(board.fields[fieldnumber].number))
  else :
    print("else")
    for j in range(1, Constant.MAX_ELEMENT + 1):
      if j == 1:
        tr1 = tbody.add(tr())
        tr1.add(th())
      tr1.add(th(Common.numberToColumnName(j, Constant.MAX_ELEMENT)))

#tr1 = tbody.add(tr())
#th1 = tr1.add(th())
#td1 = th1.add(td())
#td2 = th1.add(td())
#td3 = th1.add(td())
#td4 = th1.add(td())
#td5 = th1.add(td())
#td6 = th1.add(td())
#td7 = th1.add(td())
#td8 = th1.add(td())
print(page)
print('ok4')
path = pathlib.Path(__file__).parent.absolute()
sb = os.path.join(path, "sb")
filename = os.path.join(sb, "tst.html")
print(filename)

f = open(filename, "w")
f.write(str(page))
f.close()
import pathlib
import os
import Constant
import Common
from dominate.tags import html, body, table, tbody, tr, th, td

def createHtmlFile(filename, board):
  for i in range(len(board.fields)):
    #print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())
    _page = html()
    _body = _page.add(body())
    _table = _body.add(table())
    _tbody = _table.add(tbody())
    maxLineBoard = Constant.MAX_ELEMENT + 1
    maxLine = maxLineBoard + 1
    
    for i in range(1, maxLine):
      if (i < maxLineBoard):    
        _tr = _tbody.add(tr())
        line = Constant.MAX_ELEMENT + 1 - i
        for j in range(1, Constant.MAX_ELEMENT + 1):      
          if j == 1: 
            _tr.add(th(line))
          fieldnumber = Common.getFieldnumber(line, j, Constant.MAX_ELEMENT)
          _tr.add(td(board.fields[fieldnumber].number))
      else :
        for j in range(1, Constant.MAX_ELEMENT + 1):
          if j == 1:
            _tr = _tbody.add(tr())
            _tr.add(th())
          _tr.add(th(Common.numberToColumnName(j, Constant.MAX_ELEMENT)))
  
  path = pathlib.Path(__file__).parent.absolute()
  sb = os.path.join(path, "sb")
  filename = os.path.join(sb, filename)

  f = open(filename, "w")
  f.write(str(_page))
  f.close()

def createHtmlFileFlipped(filename, board):
  for i in range(len(board.fields)):
    #print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())
    _page = html()
    _body = _page.add(body())
    _table = _body.add(table())
    _tbody = _table.add(tbody())
    maxLineBoard = Constant.MAX_ELEMENT + 1
    maxLine = maxLineBoard + 1
    
    for i in range(1, maxLine):
      if (i < maxLineBoard):    
        _tr = _tbody.add(tr())
        line = i
        for j in range(1, Constant.MAX_ELEMENT + 1):      
          if j == 1: 
            _tr.add(th(line))
          fieldnumber = Common.getFieldnumberFlipped(line, j, Constant.MAX_ELEMENT)
          _tr.add(td(board.fields[fieldnumber].number))
      else :
        for j in range(Constant.MAX_ELEMENT, 0, -1):
          if j == Constant.MAX_ELEMENT:
            _tr = _tbody.add(tr())
            _tr.add(th())
          _tr.add(th(Common.numberToColumnName(j, Constant.MAX_ELEMENT)))
  
  path = pathlib.Path(__file__).parent.absolute()
  sb = os.path.join(path, "sb")
  filename = os.path.join(sb, filename)

  f = open(filename, "w")
  f.write(str(_page))
  f.close()
import pathlib
import os
import Constant
import Common
import dominate
from dominate.tags import link, html, body, table, tbody, tr, th, td

def createHtmlFile(filename, board):
  _page = dominate.document(title='Chess board')

  with _page.head:
   link(rel='stylesheet', href='../css/style.css')

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
        fieldContent = board.fields[fieldnumber].name
        if board.fields[fieldnumber].piece != None:
          fieldContent = board.fields[fieldnumber].piece.shortNameColor
                    
        _td = td(fieldContent, cls = board.fields[fieldnumber].color.name)
        _tr.add(_td)
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
  _page = dominate.document(title='Chess board')

  with _page.head:
   link(rel='stylesheet', href='../css/style.css')

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
        _td = td(board.fields[fieldnumber].number, cls = board.fields[fieldnumber].color.name)
        _tr.add(_td)
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
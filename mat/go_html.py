import pathlib
import os
import Constant
import Common
import Output
from Board import Board
#import dominate
#from dominate.tags import html, body, table, tbody, tr, th, td

board = Board('First', Constant.MAX_ELEMENT)
print('Allo, allo my name is ' + board.name)
print('I have ' + str(board.maxField()) + ' fields')

Output.createHtmlFile('test.html', board)
#Output.createHtmlFileFlipped('testflipped.html', board)
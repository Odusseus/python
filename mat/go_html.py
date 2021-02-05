import Constant
import Output
from Board import Board
from Config import Config

config = Config()
board = Board(config, 'First')
print('Allo, allo my name is ' + board.name)
#print('I have ' + str(board.maxField()) + ' fields')

Output.createHtmlFile('test.html', board)
#Output.createHtmlFileFlipped('testflipped.html', board)
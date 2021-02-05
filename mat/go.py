import Constant
from Config import Config
from Board import Board
config = Config()
board = Board(config, 'First')
print('Allo, allo my name is ' + board.name)
print('I have ' + str(board.getMaxField()) + ' fields')

for i in range(len(board.fields)):
 print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())
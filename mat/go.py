import Constant
import Config
from Board import Board
Config.Init()
board = Board('First')
print('Allo, allo my name is ' + board.name)
print('I have ' + str(board.getMaxField()) + ' fields')

for i in range(len(board.fields)):
 print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())
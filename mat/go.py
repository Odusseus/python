from Board import Board
board = Board('First', 8)
print('Allo, allo my name is ' + board.name)
print('I have ' + str(board.maxField()) + ' fields')

for i in range(len(board.fields)):
 print(str(board.fields[i].number) + ' ' + board.fields[i].color.name+ ' ' + board.fields[i].name())

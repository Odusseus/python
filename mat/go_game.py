import Output
from Game import Game

game = Game()

Output.createHtmlFile('game.html', game.board)
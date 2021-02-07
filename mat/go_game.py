import Config
import Output
from Game import Game

Config.Init(30, 1, True)

game = Game()

Output.createHtmlFile('game.html', game.board)
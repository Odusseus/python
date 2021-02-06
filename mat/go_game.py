import Output
from Game import Game
from Config import Config

config = Config(30, True)


game = Game(config)

Output.createHtmlFile('game.html', game.board)
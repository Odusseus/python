import Output
from Game import Game
from Config import Config

config = Config()

game = Game(config)

Output.createHtmlFile('game.html', game.board)
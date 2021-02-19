import random
from collections import deque
import Config
import Constant
import Output
from Color import Color
from Board import Board
from Box import Box
from Player import Player

class GameKing:
  def __init__(self):
    self.board = Board('First')
    self.playerWhite = Player('Ger', Constant.WHITE, self.board)
    self.playerBlack = Player('Pascal', Constant.BLACK, self.board)
    self.box = Box()
  
    if Config.random:
      fields = list(range(1, (Config.maxElement * Config.maxElement) + 1))
      random.shuffle(fields)

      if len(fields) != 0:
        self.board.addPiece(self.box.getKingWhite(fields.pop()))
      if len(fields) != 0:
        self.board.addPiece(self.box.getKingBlack(fields.pop()))

    elif Config.maxElement == 8:
      self.board.addPiece(self.box.getKingWhite('e1'))
     
      self.board.addPiece(self.box.getKingBlack('e8'))

    colorToPlay = Constant.WHITE
    while True:
      if colorToPlay == Constant.WHITE:
        self.playerWhite.play()
        colorToPlay = Constant.BLACK
      else:
        self.playerBlack.play()
        colorToPlay = Constant.WHITE

      Output.createHtmlFile('game.html', self.board)
      input("Press Enter to continue...")
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
    self.board = Board(0, 'First')
    self.playerWhite = Player('Ger', Constant.WHITE, self.board)
    self.playerBlack = Player('Pascal', Constant.BLACK, self.board)
    self.box = Box()
  
    if Config.random:
      fields = list(range(1, (Config.maxElement * Config.maxElement) + 1))
      random.shuffle(fields)

      if len(fields) != 0:
        self.board.setPiece(self.box.getKingWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getKingBlack(fields.pop()))

    elif Config.maxElement == 8:
      self.board.setPiece(self.box.getKingWhite('e1'))
     
      self.board.setPiece(self.box.getKingBlack('e8'))

    colorToPlay = Constant.WHITE
    while True:
      if colorToPlay == Constant.WHITE:
        move = self.playerWhite.play()
        colorToPlay = Constant.BLACK
      else:
        move = self.playerBlack.play()
        colorToPlay = Constant.WHITE
      if move == None:
        break
      self.board.play(move)

      Output.createHtmlFile('game.html', self.board)
      input("Press Enter to continue...")
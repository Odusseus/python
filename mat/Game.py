import Config
import Constant
import random
from Board import Board
from Box import Box
#from collections import deque
from Player import Player

class Game:
  def __init__(self):
    self.playerW = Player('Ger', Constant.WHITE)
    self.playerB = Player('Pascal', Constant.BLACK)
    self.board = Board('First')
    self.box = Box()
  
    if Config.random:
      fields = list(range(1, (Config.maxElement * Config.maxElement) + 1))
      random.shuffle(fields)

      if len(fields) != 0:
        self.board.setPiece(self.box.getKingWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getKingBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getQueenWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getQueenBlack(fields.pop()))
  
      if len(fields) != 0:
        self.board.setPiece(self.box.getRookWhite(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getRookBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getRookWhite(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getRookBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getBishopWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getBishopBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getBishopWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getBishopBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getKnightWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getKnightBlack(fields.pop()))

      if len(fields) != 0:
        self.board.setPiece(self.box.getKnightWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getKnightBlack(fields.pop()))

      #1
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #2
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #3
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #4
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #5
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #6
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #7
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

      #8
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnWhite(fields.pop()))
      if len(fields) != 0:
        self.board.setPiece(self.box.getPawnBlack(fields.pop()))

    elif Config.maxElement == 8:
      self.board.setPiece(self.box.getRookWhite('a1'))
      self.board.setPiece(self.box.getKnightWhite('b1'))
      self.board.setPiece(self.box.getBishopWhite('c1'))
      self.board.setPiece(self.box.getQueenWhite('d1'))
      self.board.setPiece(self.box.getKingWhite('e1'))
      self.board.setPiece(self.box.getBishopWhite('f1'))
      self.board.setPiece(self.box.getKnightWhite('g1'))
      self.board.setPiece(self.box.getRookWhite('h1'))
     
      self.board.setPiece(self.box.getPawnWhite('a2'))
      self.board.setPiece(self.box.getPawnWhite('b2'))
      self.board.setPiece(self.box.getPawnWhite('c2'))
      self.board.setPiece(self.box.getPawnWhite('d2'))
      self.board.setPiece(self.box.getPawnWhite('e2'))
      self.board.setPiece(self.box.getPawnWhite('f2'))
      self.board.setPiece(self.box.getPawnWhite('g2'))
      self.board.setPiece(self.box.getPawnWhite('h2'))
     
      self.board.setPiece(self.box.getRookBlack('a8'))
      self.board.setPiece(self.box.getKnightBlack('b8'))
      self.board.setPiece(self.box.getBishopBlack('c8'))
      self.board.setPiece(self.box.getQueenBlack('d8'))
      self.board.setPiece(self.box.getKingBlack('e8'))
      self.board.setPiece(self.box.getBishopBlack('f8'))
      self.board.setPiece(self.box.getKnightBlack('g8'))
      self.board.setPiece(self.box.getRookBlack('h8'))
     
      self.board.setPiece(self.box.getPawnBlack('a7'))
      self.board.setPiece(self.box.getPawnBlack('b7'))
      self.board.setPiece(self.box.getPawnBlack('c7'))
      self.board.setPiece(self.box.getPawnBlack('d7'))
      self.board.setPiece(self.box.getPawnBlack('e7'))
      self.board.setPiece(self.box.getPawnBlack('f7'))
      self.board.setPiece(self.box.getPawnBlack('g7'))
      self.board.setPiece(self.box.getPawnBlack('h7'))
     
    elif Config.maxElement > 8:
      self.board.setPiece(self.box.getRookWhite(1))
      self.board.setPiece(self.box.getKnightWhite(2))
      self.board.setPiece(self.box.getBishopWhite(3))
      self.board.setPiece(self.box.getQueenWhite(4))
      self.board.setPiece(self.box.getKingWhite(5))
      self.board.setPiece(self.box.getBishopWhite(6))
      self.board.setPiece(self.box.getKnightWhite(7))
      self.board.setPiece(self.box.getRookWhite(8))
     
      self.board.setPiece(self.box.getPawnWhite(9))
      self.board.setPiece(self.box.getPawnWhite(10))
      self.board.setPiece(self.box.getPawnWhite(11))
      self.board.setPiece(self.box.getPawnWhite(12))
      self.board.setPiece(self.box.getPawnWhite(13))
      self.board.setPiece(self.box.getPawnWhite(14))
      self.board.setPiece(self.box.getPawnWhite(15))
      self.board.setPiece(self.box.getPawnWhite(16))
     
      self.board.setPiece(self.box.getRookBlack(49))
      self.board.setPiece(self.box.getKnightBlack(50))
      self.board.setPiece(self.box.getBishopBlack(51))
      self.board.setPiece(self.box.getQueenBlack(52))
      self.board.setPiece(self.box.getKingBlack(53))
      self.board.setPiece(self.box.getBishopBlack(54))
      self.board.setPiece(self.box.getKnightBlack(55))
      self.board.setPiece(self.box.getRookBlack(56))
     
      self.board.setPiece(self.box.getPawnBlack(57))
      self.board.setPiece(self.box.getPawnBlack(58))
      self.board.setPiece(self.box.getPawnBlack(59))
      self.board.setPiece(self.box.getPawnBlack(60))
      self.board.setPiece(self.box.getPawnBlack(61))
      self.board.setPiece(self.box.getPawnBlack(62))
      self.board.setPiece(self.box.getPawnBlack(63))
      self.board.setPiece(self.box.getPawnBlack(64))
import Constant
from Board import Board
from Box import Box
from Player import Player

class Game:
  def __init__(self):
   self.playerW = Player('W', Constant.WHITE)
   self.playerB = Player('B', Constant.BLACK)
   self.board = Board(Constant.MAX_ELEMENT, 'First')
   self.box = Box()
   
   self.board.addPiece(self.box.getRookWhite('a1'))
   self.board.addPiece(self.box.getKnightWhite('b1'))
   self.board.addPiece(self.box.getBishopWhite('c1'))
   self.board.addPiece(self.box.getQueenWhite('d1'))
   self.board.addPiece(self.box.getKingWhite('e1'))
   self.board.addPiece(self.box.getBishopWhite('f1'))
   self.board.addPiece(self.box.getKnightWhite('g1'))
   self.board.addPiece(self.box.getRookWhite('h1'))

   self.board.addPiece(self.box.getPawnWhite('a2'))
   self.board.addPiece(self.box.getPawnWhite('b2'))
   self.board.addPiece(self.box.getPawnWhite('c2'))
   self.board.addPiece(self.box.getPawnWhite('d2'))
   self.board.addPiece(self.box.getPawnWhite('e2'))
   self.board.addPiece(self.box.getPawnWhite('f2'))
   self.board.addPiece(self.box.getPawnWhite('g2'))
   self.board.addPiece(self.box.getPawnWhite('h2'))

   self.board.addPiece(self.box.getRookBlack('a8'))
   self.board.addPiece(self.box.getKnightBlack('b8'))
   self.board.addPiece(self.box.getBishopBlack('c8'))
   self.board.addPiece(self.box.getQueenBlack('d8'))
   self.board.addPiece(self.box.getKingBlack('e8'))
   self.board.addPiece(self.box.getBishopBlack('f8'))
   self.board.addPiece(self.box.getKnightBlack('g8'))
   self.board.addPiece(self.box.getRookBlack('h8'))

   self.board.addPiece(self.box.getPawnBlack('a7'))
   self.board.addPiece(self.box.getPawnBlack('b7'))
   self.board.addPiece(self.box.getPawnBlack('c7'))
   self.board.addPiece(self.box.getPawnBlack('d7'))
   self.board.addPiece(self.box.getPawnBlack('e7'))
   self.board.addPiece(self.box.getPawnBlack('f7'))
   self.board.addPiece(self.box.getPawnBlack('g7'))
   self.board.addPiece(self.box.getPawnBlack('h7'))

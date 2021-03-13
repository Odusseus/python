from random import random, randrange
from Color import Color
from Board import Board
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Field import Field
from Move import Move
import Constant

class Player:
  def __init__(self, name, colorCode, board = None):
   assert name != None
   assert colorCode != None
   
   self.name = name
   self.color = Color(colorCode)
   
   if board != None:
     self.board = board 
   else:
     self.board = Board()

  def play(self):
    myPieces = self.board.getPieces(self.color)
    candidateBoards = []
    for myPiece in myPieces: 
      reachs = myPiece.getCurrentReachs()
      candidateMoves = []
      for reachFieldId in reachs:
        # field = self.board.fields[reachFieldId]
        # if field.piece != None and field.piece.color.id == myPiece.color.id:
        #   break
        newField = Field(reachFieldId)
        # if field.piece != None and field.piece.color.id != myPiece.color.id:
        #   newField.piece = field.piece
        candidateMoves.append(newField)

      for candidateMove in candidateMoves:  
        board = self.board.clone()
        move = Move(myPiece.field.id, candidateMove.id)
        board.play(move)
        if (board.isCheck(self.color.id) == True):
          continue
        else:          
          board.evaluate() 
          candidateBoards.append(board)

      if len(candidateBoards) == 0:
        return None
      

      if len(candidateBoards) == 1:
        return candidateBoards[0].lastMove

      if self.color.id == Constant.WHITE:
        sorted(candidateBoards, key=lambda board: board.value)
      else:
        sorted(candidateBoards, key=lambda board: -board.value)
      
      maxValue = candidateBoards[0].value
      maxValueCandidateBoards = []
      for candidateBoard in candidateBoards:
        if candidateBoard.value == maxValue:
          maxValueCandidateBoards.append(candidateBoard)
        else:
          break
      randomBoard = randrange(len(maxValueCandidateBoards) - 1)
      return candidateBoards[randomBoard].lastMove

      # if len(candidateBoards) > 0:
      #   if self.color.id == Constant.WHITE:
      #     index = 0
      #   else:
      #     index = len(candidateBoards) - 1
      #   return candidateBoards[index].lastMove
      #else:
       #return None
        
    return None

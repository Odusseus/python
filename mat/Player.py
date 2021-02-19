from Color import Color
from Board import Board
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Field import Field

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
    allPieces = self.board.getAllPieces()
    myBoard = Board()

    for allPiece in allPieces:
      if isinstance(allPiece, King):
        piece = King(
                allPiece.color.id,
                allPiece.code,
                allPiece.field.id)
        piece.reachs = allPiece.reachs
      elif isinstance(allPiece, Queen):
        raise TypeError("Argument type not implementated.")
           
      elif isinstance(allPiece, Rook):
        raise TypeError("Argument type not implementated.")
           
      elif isinstance(allPiece, Bishop):
        raise TypeError("Argument type not implementated.")
           
      elif isinstance(allPiece, Knight):
        raise TypeError("Argument type not implementated.")
           
      elif isinstance(allPiece, Pawn):
        raise TypeError("Argument type not implementated.")
           
      else:
        raise TypeError("Wrong argument type.")       
      myBoard.addPiece(piece)
    myPieces = myBoard.getPieces(self.color)
    myPiece = myPieces[0]
    reachs = myPiece.getReachs()
    candidateMoves = []
    for reachFieldId in reachs:
      field = myBoard.fields[reachFieldId]
      if field.piece != None and field.piece.color.id == myPiece.color.id:
       continue
      newField = Field(reachFieldId)
      if field.piece != None and field.piece.color.id != myPiece.color.id:
        newField.piece = field.piece
      candidateMoves.append(newField);    
    
    # TODO
    # fields = []
    # for i in range(1, myBoard.getMaxField() + 1):
    #   if i == 1:
    #     fields.append(Field(0)) # Field 0 doesn't exist
    #   fields.append(Field(i))

    # otherColor =  self.color.getOpposite()
    # otherPieces = myBoard.getPieces(otherColor)
    # for otherPiece in otherPieces:
    #   reachs = otherPiece.getReachs()
    #   for reachFieldId in reachs:
    #   fields[reachFieldId] = 
    
    
    return myPiece

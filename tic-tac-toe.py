import math
import time
from players import HumanPlayer, ComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    def make_board():
        return [' ' for i in range(9)]
    
    def move(self,letter,square):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.win(square,letter):
                self.winner = letter
            return True
        return False
    
    def print_board(self):
        for i in self.board:
            if()


    #check if win conditions are fulfilled
    def win(self,square,letter):
        #check if letters in row are all the same
        row=self.board[math.floor(square/3):(math.floor(square/3)+1)*3] 
        if all(i == letter for i in row):
            return True
        
        #check if letters in column are all the same
        col = [self.board[square + i*3] for i in range(3)]
        if all([i == letter for i in col]):
            return True
        
        #check if letters in diagonal are all the same
        if square in(0,4,8):
            diagonal=[self.board[0+i*4] for i in range(3)]
            if all([i == letter for i in diagonal]):
                return True
        if square in(2,4,6):
            diagonal=[self.board[2+i*2] for i in range(3)]
            if all([i == letter for i in diagonal]):
                return True



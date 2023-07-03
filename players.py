import math
import random

class Player:

    def __init__(self,letter):
        self.letter = letter

    def get_move(self,game):
        pass

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + "'s turn. Input one number 0-9: ")
            try:

            

class ComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return super().get_move(game)
     
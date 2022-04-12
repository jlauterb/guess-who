"""INST326 Final Project Group (pp)enguin for Sana, Janet, Sierra, and John """
import random

class Player():
    """Class that represents a player in the guess who game
    """
    
    def __init__(self, name):
        #Player's name
        self.name = name
        """
        Celebrity list for the board will be a dictionary with the name,
        in all uppercase, as the key.
        The value of each key with be a tuple of the aspects that a 
        player can use to ask questions about.
        """
        self.board = {"Celebrity 1": ("Aspect 1","Aspect 2"),
                      "Celebrity 2": ("Aspect 1","Aspect 2"),
                      "Celebrity 3": ("Aspect 1","Aspect 2"),
                      "Celebrity 4": ("Aspect 1","Aspect 2"),
                      "Celebrity 5": ("Aspect 1","Aspect 2"),
                      "Celebrity 6": ("Aspect 1","Aspect 2"),
                      "Celebrity 7": ("Aspect 1","Aspect 2"),
                      "Celebrity 8": ("Aspect 1","Aspect 2"),
                      "Celebrity 9": ("Aspect 1","Aspect 2"),
                      "Celebrity 10": ("Aspect 1","Aspect 2"),
                      "Celebrity 11": ("Aspect 1","Aspect 2"),
                      "Celebrity 12": ("Aspect 1","Aspect 2"),
                      "Celebrity 13": ("Aspect 1","Aspect 2"),
                      "Celebrity 14": ("Aspect 1","Aspect 2"),
                      "Celebrity 15": ("Aspect 1","Aspect 2"),
                      "Celebrity 16": ("Aspect 1","Aspect 2"),
                      "Celebrity 16": ("Aspect 1","Aspect 2"),
                      "Celebrity 17": ("Aspect 1","Aspect 2"),
                      "Celebrity 18": ("Aspect 1","Aspect 2"),
                      "Celebrity 19": ("Aspect 1","Aspect 2"),
                      "Celebrity 20": ("Aspect 1","Aspect 2"),
                      }
        #Player's list of celebrities it could not be
        self.rejected = []
        #Player's celebrity that another player will try to guess
        self.assigned_celebrity = random.choice(self.board)


class GuessWho:
    """
    Basic class to share
    
    Attributes:

    """
    
    def __init__(self, player1, player2):
        #List of the players
        self.players = [player1, player2]
        self.celebrities_needed = [player1.assigned_celebrity,
                                   player2.assigned_celebrity]
    

    def turn(self):
        #represents one players turn

if __name__ == "__main__":
    #Line to run the program
    player1 = Player(input("Player 1 enter your name:"))
    player2 = Player(input("Player 2 enter your name:"))
    GuessWho(player1, player2)
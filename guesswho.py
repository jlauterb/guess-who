"""INST326 Final Project Group (pp)enguin for Sana, Janet, Sierra, and John """
from multiprocessing.sharedctypes import Value
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
        """initializes the attributes.

        Args:
            player1(str): represents the first player.
            player2(str): represents the second player.

        Side effects:
            opens a file containing the names of the celebrities.
        """
        #List of the players
        self.celebrities = []
        with open(filename, "r", encoding = "utf-8") as file:
            for line in file:
                self.celebrities = self.celebrities_needed


        self.players = [player1, player2]
        self.celebrities_needed = [player1.assigned_celebrity,
                                   player2.assigned_celebrity]

    
    def final_q(self, player):
        return "ur mom"
        
    def trait_q(self, player):
        return "deez nuts"
    
    def turn(self, player):
        #represents one players turn
        question_type = input("What type of question would you like to ask? (type 0 to guess a trait, 1 to guess a celeb")
        if question_type == "0":
            #call trait question method
            trait_q(player)
        else:
            #call final question method
            final_q(player)
        
        if question_type != "0" | question_type != "1":
            raise ValueError("Sorry, please input a 0 or a 1")
        
    def winner(self):
        if final_g(player1) == player1.assigned_celebrity:
            print(f"{player1} wins with the guess of {player1.assigned_celebrity}!")
        elif final_g(player2) == player2.assigned_celebrity:
            print(f"{player2} wins with the guess of {player2.assigned_celebrity}!")
        else
            print(f"{player1} and {player2} both lost!")
        
    
    
    

if __name__ == "__main__":
    #Line to run the program
    player1 = Player(input("Player 1 enter your name:"))
    player2 = Player(input("Player 2 enter your name:"))
    GuessWho(player1, player2)
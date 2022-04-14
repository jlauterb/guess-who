"""INST326 Final Project Group (pp)enguin for Sana, Janet, Sierra, and John """
import random
import csv
from argparse import ArgumentParser
import sys

class Board():
    """Representation of Guess Who board.
    
    Attributes:
    name_board(dict): Contains celebrity names and attributes
    """
    
    def __init__(self, filename):
        """Initalizes the board from a csv file

        Args:
            filename (str): File path to csv file
        """
        brd = {}
        #Hopefully, this will turn a csv file into a dict where the first column is a key,
        #The rest of the columns will turn into 1 tuple as the value of the key.
        with open(filename, newline = ' ') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row.pop(0)
                data = tuple()
                [data.add(col) for col in row]
            brd[name] = data
    
    def greeting(self, game="Guess Who", coders="John, Sierra, Janet, and Sana", end="!"):
        """greets the players at the start of the game.

        Args:
            game(str): the name of the game
            end(str): ends the print statement with an exclamation mark
            coders(str): the names of the people in our group
            
        Side effects:
            a greeting to begin the game

        """
        print("Hello, and welcome to the game of", game, "coded by", coders)


    print(greeting())

            
        
        
    
class Player():
    """Class that represents a player in the guess who game
    
    Attributes:
    name (str): Name of the player
    board (dict): Contains celebrity names and attributes
    rejected(list): Contains celebrities that are not the assigned celebrity
    assigned_celebrity(str): The celebrity that an opponent will try to guess
    """
    
    def __init__(self, name, board):
        """Initalizes the Player class.
        
        Args:
        name (str): Name of the player
        
        Side Effects:
        Changes the classes attributes
        """
        #Player's name
        self.name = name
        #Board from Board class
        self.board = board
        #Player's list of celebrities it could not be
        self.rejected = []
        #Player's celebrity that another player will try to guess
        self.assigned_celebrity = random.choice(self.board)


class GuessWho:
    """Guess Who game.
    
    Attributes:
    players (list): list of player objects
    celebrities ()

    """
    
    def __init__(self, player1, player2, filename):
        """initializes the attributes.

        Args:
            player1(str): represents the first player.
            player2(str): represents the second player.

        Side effects:
            opens a file containing the names of the celebrities.
        """

        self.players = [player1, player2]
        self.celebrities_needed = [player1.assigned_celebrity,
                                   player2.assigned_celebrity]

    
    def final_q(self, player):
        """Represents the final question that the players may ask.
        """
        return player
        
    def trait_q(self, player):
        """Questions related to traits that the celebrities may have.
        """

        return player
    
    def turn(self, player):
        """This method represents the turns between each player.

        Raises:
            ValueError for invalid question type.
        """
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
        """This method determines who wins in the game, if any player guesses the celebrity correctly.
        """
        if final_q(player1) == player1.assigned_celebrity:
            print(f"{player1} wins with the guess of {player1.assigned_celebrity}!")
        elif final_q(player2) == player2.assigned_celebrity:
            print(f"{player2} wins with the guess of {player2.assigned_celebrity}!")
        else:
            print(f"{player1} and {player2} both lost!")

def parse_args(arglist):
    """Parse command-line arguments. 
    Expect one mandatory argument, the path to a file of celebrity names and attributes.

    Args:
        arglist (list of str): command-line arguments

    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to csv file with celebrity names and attributes")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    #Line to run the program
    
    args = parse_args(sys.args[1:])
    
    Board(args)
    
    player1 = Player(input("Player 1 enter your name:"))
    player2 = Player(input("Player 2 enter your name:"))
    GuessWho(player1, player2)
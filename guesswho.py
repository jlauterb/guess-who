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
        self.brd = {}
        #Hopefully, this will turn a csv file into a dict where the first column is a key,
        #The rest of the columns will turn into 1 tuple as the value of the key.
        with open(filename, newline = ' ') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row.pop(0)
                data = tuple()
                [data.add(col) for col in row]
            self.brd[name] = data
    
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
        
        
    def __str__(self):
        return str(self.brd.keys)


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
        
        
    def __str__(self):
        """Gives the name of the player when called.

        Returns:
            name(str): player's name
        """
        return self.name


class GuessWho:
    """Guess Who game.
    
    Attributes:
    players(list): list of player objects
    celebrities_needed(list): description of the player's celebrity the opponent needs to guess.

    """
    
    def __init__(self, player1, player2):
        """initializes the attributes.

        Args:
            player1(str): represents the first player.
            player2(str): represents the second player.

        Side effects:
            opens a file containing the names of the celebrities.
        """
        self.players = [player1, player2]

    
    def final_q(self, player):
        """Represents the final question that the players may ask.

        Returns:
            boolean: did they guess the celebrity correctly
        """
        response = input("Enter your celebrity guess:").upper()
        return (response == self.players[player].assigned_celebrity)
        
        
    def trait_q(self, player):
        """Questions related to traits that the celebrities may have.

        Returns:
            the player object
        """
        category_response = input("Pick a category: Industry, Facial Hair, " +
                "Presenting, Eye Color, Hair Color, Hair Length, Controversy, "
                + "and Height").upper()
        if category_response == "INDUSTRY":
            choice_response = input("Pick a choice: Music, "
                                    + "Reality, Acting").upper()
            category_response = 0
        elif category_response == "FACIAL HAIR":
            choice_response = input("Pick a choice: No Facial Hair, Beard, Goatee").upper()
            category_response = 1
        elif category_response == "PRESENTING":
            choice_response = input("Pick a choice: Male, Female").upper()
            category_response = 2
        elif category_response == "EYE COLOR":
            choice_response = input("Pick a choice: Brown, Hazel, Green, Blue, Black").upper()
            category_response = 3
        elif category_response == "HAIR COLOR":
            choice_response = input("Pick a choice: Black, Brown, Blond, Ginger").upper()
            category_response = 4
        elif category_response == "HAIR LENGTH":
            choice_response = input("Pick a choice: Short, Medium, Long").upper()
            category_response = 5
        elif category_response == "CONTROVERSY":
            choice_response = input("Pick a choice: Controversial, Not Controversial").upper()
            category_response = 6
        elif category_response == "HEIGHT":
            choice_response = input("Pick a choice: Short, Average, Tall").upper()
            category_response = 7
            
        return player
    
    def turn(self, player):
        """This method represents the turns between each player.

        """
        question_type = input("What type of question would you like to ask? (type 0 to guess a trait, 1 to guess a celeb")
        
        #Invalid response will call the method again for the same player
        if question_type != "0" | question_type != "1":
            self.turn(player)
         
        #call trait question method   
        if question_type == "0":
            self.trait_q(player)
            player = abs(player - 1)
            self.turn(player)
            
        else:
            #call final question method
            self.winner(player)
        
        
    def winner(self, player):
        """This method determines who wins in the game, if any player guesses the celebrity correctly.
        
        Side effects:
            prints if either player1 wins, player2 wins, or if both players lose
        """
        
        #Player whose turn it guessing the final celeb
        curr_player = self.players[player]
        if self.final_q(player):
            print(f"{str(curr_player)} wins with the guess of {curr_player.assigned_celebrity}!")
        
        #Changes to the next player to guess
        else:
            curr_player = self.players[abs(player - 1)]
            if self.final_q(player):
                print(f"{str(curr_player)} wins with the guess of {curr_player.assigned_celebrity}!") 
                 
            #Neither player guessed correctly, both lost
            else:
                print(f"{self.players[0]} and {self.players[1]} both lost!")


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
    
    celebs = Board(args)
    
    player1 = Player(input("Player 1 enter your name:"),celebs)
    player2 = Player(input("Player 2 enter your name:"),celebs)
    GuessWho(player1, player2)
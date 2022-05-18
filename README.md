# guess-who
INST326 Final Project

An explanation of the purpose of each file in repository:
.gitignore: files that Git ignores
License: copyright for our program under the GNU general public license 
README.md: the markdown file in our repository
Celebrities.csv: the csv file of the names of celebrities and their traits that we utilized in our program
Guesswho.py: the python file of our program 

Instructions on how to run program from the command line:
For Mac users:
python3 guesswho.py celebrities.csv

For Windows users:
python guesswho.py celebrities.csv

How to use your program and/or interpret the output of the program, as applicable:

In our Guess Who game, there are two players. Each player is assigned one random celebrity out of a list of 20 pre-selected celebrities that they have to guess. When it is a player’s turn, they have the opportunity to either ask about a trait of their chosen celebrity, or make a final guess on who the celebrity is. Each time a player asks a trait question, their list of celebrities is printed out to show how it changed, and which celebrities they are left to choose from. A player wins if they can correctly guess who their randomly assigned celebrity is before the other player. 


__init__ method in Board class: Janet
Greeting method in Board class: Sana
__str__ method in Board class: Sierra

__init__ method in Player class: John
__str__ method in Player class: John

__init__ method in GuessWho class: Sana
final_q method in GuessWho class: Sierra
trait_q method in GuessWho class: Sierra
print_board method in GuessWho class: Janet
turn method in GuessWho class: John
winner method in GuessWho class: Sana

parse_args method: Janet

conditional expressions - John 
optional parameters and/or use of keyword arguments - Sana 
F-strings - Sana
with statements - John
the ArgumentParser class - Janet
comprehensions or generator expressions - Sierra
custom list sorting with a key function (possibly a lambda expression) - Janet
magic methods other than __init__() - Sierra 

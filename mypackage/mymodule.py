
"""
A function for playing rock paper scissors
"""

import random


def playRPS(throw):
    """
    returns the result of one round of RPS
    """

    #set up computer throw
    possibleThrows = ["rock","paper","scissors"]
    compThrow = random.choice(possibleThrows)

    # get and format user throw
    if(isinstance(throw, (str)) and (throw == "rock" or throw == "paper" or throw == "scissors")):
    	myThrow = throw.lower()
    	calculateWinner(myThrow, compThrow)

    else:
    	print("Please type in 'rock','paper', or 'scissors'")


def calculateWinner(throw1,throw2):
    #set up winner matrix
    throwDict = {"rock" : 0, "paper" : 1, "scissors" : 2}
    winner = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
    ]

    win = winner[throwDict[throw1]][throwDict[throw2]]

    print("You threw: " + throw1)
    print("I threw: " + throw2)

    if(win == 1):
    	print("Darn it, you beat me!")
    elif(win == -1):
    	print("HAHA I WIN")
    else:
    	print("It's a tie!")


if __name__ == "__main__":
    possibleThrows = ["rock","paper","scissors"]
    playRPS(random.choice(possibleThrows))

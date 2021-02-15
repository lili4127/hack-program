
"""
A class for playing rock paper scissors
"""

import numpy as np
import pandas as pd

possibleThrows = np.array(["rock","paper","scissors"])

#computer plays 100 games against itself and records all the winning throws to csv by round. This
#is mimicing a professional's throwing record saved on file 
def makeRecord():

    throwList = []

    for i in range(100):
        throw1 = np.random.choice(possibleThrows)
        throw2 = np.random.choice(possibleThrows)

        if (calculateWinner(throw1, throw2) == 1):
            throwList.append(throw1)
        elif (calculateWinner(throw1, throw2) == -1):
            throwList.append(throw2)
        else:
            throwList.append(throw1)

    throwDF = pd.DataFrame(throwList)
    throwDF.to_csv('record.csv',index = False)

#take in a csv of a record of someone's throws and find the best throw to counter
#that person
def learnFrom(throwRecord):
    throws = pd.read_csv(throwRecord, names = ['throw'])
    print(throws)
    print('-----')

    mostUsedThrow = throws.mode()['throw'][0]
    print("most used throw: " + mostUsedThrow)
    print('-----')

    return mostUsedThrow

def playRPS(throw):
    """
    returns the result of one round of RPS
    """

    #set up computer throw from a record of opponent's throws. pick throw to beat their
    #most commonly used throw

    throwToBeat = learnFrom('record.csv')

    if(throwToBeat == 'rock'):
        compThrow = 'paper'

    elif(throwToBeat == 'paper'):
        compThrow = 'scissors'

    else:
        compThrow = 'rock'

    # get and format user throw
    if(isinstance(throw, (str)) and (throw == "rock" or throw == "paper" or throw == "scissors")):
        userThrow = throw.lower()
        print("You threw: " + userThrow)
        print("I threw: " + compThrow)
        printWinner(calculateWinner(userThrow, compThrow))

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

    return winner[throwDict[throw1]][throwDict[throw2]]

#prints the winner based on winner matrix above (relative to throw1)
def printWinner(win):

    if(win == 1):
    	print("Darn it, you beat me!")
    elif(win == -1):
    	print("HAHA I WIN")
    else:
    	print("It's a tie!")


if __name__ == "__main__":
    makeRecord()
    playRPS(np.random.choice(possibleThrows))

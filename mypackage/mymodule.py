#!/usr/bin/env python

"""
A module for playing rock paper scissors lizard spock after learning
"""

import numpy as np
import pandas as pd

POSSIBLE_THROWS = np.array(["rock", "paper", "scissors", "lizard", "spock"])
WINNER = np.array([
    [0, -1, 1, 1, -1],
    [1, 0, -1, -1, 1],
    [ -1, 1, 0, 1, -1],
    [ -1, 1, -1, 0, 1],
    [1, -1, 1, -1, 0]
    ])
INDEX = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4,}

def make_record(trials=100, probs=(1/5, 1/5, 1/5, 1/5, 1/5)):
    """
    Sample 100 random throws with the results weighted by the
    person's preference/bias. Returns a 1D array of strings.

    Parameters:
    -----------
    trials: int
        Number of samples to observe.
    probs: tuple
        Five values summing to 1 representing the probability of
        sampling rock, paper, scissors, lizard, spock in that order. Default
        is 1/5 equal probability.
    """
    return np.random.choice(POSSIBLE_THROWS, size=trials, p=probs)


def learn_freqs_from(record):
    """
    Examine professional's records and estimate frequency of throws.

    Parameters:
    -----------
    record: ndarray
        Array of sampled throws with size trials and probs for each throw.
    """

    # get frequency of professional's throws
    freqs = pd.value_counts(record) / len(record)

    # recommendation is to return winner at frequency they chose loser
    # recommendation is organized in the order of rock, paper, scissors, lizard, spock
    # rock, paper, scissors, lizard, spock beats lizard, rock, paper, spock, scissors respectively
    # ex: if they chose lizard 40 percent of the time, return rock 40% of the time to beat lizard
    recommendation = [
        freqs["lizard"] if "lizard" in freqs else 0.0,      # returns rock as freq as they return lizard
        freqs["rock"] if "rock" in freqs else 0.0,          # returns paper as freq as they return rock
        freqs["paper"] if "paper" in freqs else 0.0,        # returns sciss as freq as they return paper
        freqs["spock"] if "spock" in freqs else 0.0,        # returns lizard as freq as they return spock
        freqs["scissors"] if "scissors" in freqs else 0.0,  # returns spock as freq as they return scissors
    ]

    return recommendation

def play_rpslz(trials=100, probs=(1/5, 1/5, 1/5, 1/5, 1/5)):
    """
    Play many trials of rock-paper-scissors-lizard-spock after first studying the
    frequency of the other players throws to learn their bias.

     Parameters:
    -----------
    trials: int
        Number of trials to play after having studied.
    probs: tuple
        Five values summing to 1 representing the probability of computer
        picking rock, paper, scissors, lizard, spock in that order. Default
        is 1/5 equal probability.

    """
    # sample professional's throws
    record = make_record(trials, probs)

    # get recommendations from studying
    recommend = learn_freqs_from(record)

    # keep track of wins
    wins = 0
    ties = 0

    # perform trials
    for _ in range(trials):

        # we both throw
        mine = np.random.choice(POSSIBLE_THROWS, p = recommend)
        theirs = np.random.choice(POSSIBLE_THROWS, p = probs)

        # compare
        if WINNER[INDEX[mine],INDEX[theirs]] == 0:
            ties += 1
        elif WINNER[INDEX[mine],INDEX[theirs]] == 1:
            wins += 1

        #print(mine, theirs, wins)

    # if zero wins then percentage is zero
    if not wins:
        percentage = 0.0
    else:
        percentage = round(100 * wins / (trials - ties), 2)

    # report winning
    print(f"I won {percentage}% of {trials} trials (ties={ties})")


if __name__ == "__main__":

    # play a game with equal weighting
    print("equal weighting:")
    play_rpslz(trials=1000)

    # play a game where they are biased towards rock
    print("biased weighting:")
    play_rpslz(trials=1000, probs=[0.6, 0.1, 0.1, 0.1, 0.1])

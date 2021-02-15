"""
Command line interface to mymodule
"""
import argparse
import random
from mymodule import playRPS, calculateWinner


def parse_command_line():
    "parses args for the playRPS funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "rock",
        type= str,
        help="plays a game with rock as the user throw",
        action="store_true")

    # add long args
    parser.add_argument(
        "paper",
        type= str,
        help="plays a game with paper as the user throw",
        action="store_true")

    parser.add_argument(
        "scissors",
        type= str,
        help="plays a game with scissors as the user throw",
        action="store_true")

    # parse args
    args = parser.parse_args()

    # check that user only entered one action arg
    if sum([args.rock, args.paper, args.scissors]) > 1:
        raise SystemExit(
            "only one of 'rock', 'paper' or 'scissors' at a time.")
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call darwinday function
    if args.rock:
        playRPS("rock")
    elif args.paper:
        playRPS("paper")
    elif args.scissors:
        playRPS("scissors")


if __name__ == "__main__":
    possibleThrows = ["rock","paper","scissors"]
    playRPS(random.choice(possibleThrows))
#!/usr/bin/env python

"""
Command line interface to mymodule
"""

import argparse
from mypackage.mymodule import play_rpslz


def parse_command_line():
    "parses args for the playRPS funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "-t", "--trials",
        type= int,
        default=1,
        help="number of replicate R/P/S/L/K games to play",
        action="store")

    # add long args
    parser.add_argument(
        "-p", "--probs",
        nargs=5,
        type= float,
        default=(1/5, 1/5, 1/5, 1/5, 1/5),
        help="the probability the computer chooses rock, paper, scissors, lizard, or spock",
        action="store")

    # parse args
    args = parser.parse_args()
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()
    play_rpslz(args.trials, args.probs)

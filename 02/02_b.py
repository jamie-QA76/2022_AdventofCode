# Day 2: Rock Paper Scissors
# Part 2: Calculate total score gained by following the elven gamer guide

import sys
import re

totalscore = 0

points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
    "XA": 3,
    "XB": 1,
    "XC": 2,
    "YA": 1,
    "YB": 2,
    "YC": 3,
    "ZA": 2,
    "ZB": 3,
    "ZC": 1,
    
}

def score(outcome, opp):
    total = points[outcome] + points[outcome + opp]
    return total

inputfile = sys.argv[1]

with open(inputfile, "r") as file:
    for row in file:
        # Total each together until it hits an empty line
        values = row.strip()
        opp = values[0]
        outcome = values[2]
        totalscore += score(outcome, opp)

print(totalscore)
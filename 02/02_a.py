# Day 2: Rock Paper Scissors
# Part 1: Calculate total score gained by following the elven gamer guide

import sys
import re

totalscore = 0

points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "XA": 3,
    "XB": 0,
    "XC": 6,
    "YA": 6,
    "YB": 3,
    "YC": 0,
    "ZA": 0,
    "ZB": 6,
    "ZC": 3,
    
}

def score(self, opp):
    total = points[self] + points[self + opp]
    return total

inputfile = sys.argv[1]

with open(inputfile, "r") as file:
    for row in file:
        # Total each together until it hits an empty line
        values = row.strip()
        opp = values[0]
        self = values[2]
        totalscore += score(self, opp)

print(totalscore)
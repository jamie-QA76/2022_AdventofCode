# Day 1: Calorie Countings
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying

import sys
import re

# Read in file
# Loop through each line, grabbing numeric string as a number
inputfile = sys.argv[1]
elves = {}
topthree = {}
elfcounter = 1
elves[elfcounter] = 0

def keepmax(elfcounter, calories):
    topthree[elfcounter] = calories
    if len(topthree.keys()) > 3:
        min_value = min(topthree, key=topthree.get)
        topthree.pop(min_value)
        

with open(inputfile, "r") as file:
    for row in file:
        # Total each together until it hits an empty line
        value = row.strip()
        if value == "":
            keepmax(elfcounter, elves[elfcounter])
            elfcounter += 1
            elves[elfcounter] = 0
        else:
            calories = int(value)
            elves[elfcounter] += calories
    keepmax(elfcounter, elves[elfcounter])

print(sum(topthree.values()))
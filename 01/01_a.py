# Day 1: Calorie Countings
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying

import sys
import re

# Read in file
# Loop through each line, grabbing numeric string as a number
inputfile = sys.argv[1]
elves = {}
elfcounter = 1
elves[elfcounter] = 0

with open(inputfile, "r") as file:
    for row in file:
        # Total each together until it hits an empty line
        value = row.strip()
        if value == "":
            elfcounter += 1
            elves[elfcounter] = 0
        else:
            calories = int(value)
            elves[elfcounter] += calories

max_value = max(elves, key=elves.get)

# Save the max total elf
# Print out the total Calories the Elf is carrying
print(max_value, elves[max_value])
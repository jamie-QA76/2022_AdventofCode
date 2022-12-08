# Day 05: Supply Stacks

# Given a diagram of stacked crates and instructions, move crates according to the directions
# Keep crates in order of the groups they are taken in
# Output the letters of the topmost crates.

import sys
import re

inputfile = sys.argv[1]


crates = []
instructions = [] #list of dictionaries?

# read in the whole file as lines
# use regex to find the 1 2 3 line and get the number and length
# use the number to create the crates loop
# then make the instructions loop

file = open(inputfile, 'r')
body = file.readlines()

no_crates = int(len(body[0]) / 4)

counter = 0

def movecrates(number, start, end):
    load = []
    for move in range(number):
        take = crates[start].pop(0)
        load.insert(0, take)
    for crate in load:
        crates[end].insert(0, crate)

for i in range(no_crates):
    crates.append([])

#get crate info
for line in body:
    if re.search("^\s*\[.*", line):
        for i in range(no_crates):
            crateletter = line[(i*4)+1]
            if crateletter != " ":
               crates[i].append(crateletter)
        counter += 1
    elif re.search("^\s*move.*", line):
        moves = line.split()
        instruction = [int(moves[1]), int(moves[3])-1, int(moves[5])-1]
        instructions.append(instruction)
        counter += 1
    elif re.search("^[\d\s]+$", line):
        counter += 1

for x in instructions:
    movecrates(x[0], x[1], x[2])

topcrates = ""
for c in crates:
    topcrates += c[0]
print(topcrates)
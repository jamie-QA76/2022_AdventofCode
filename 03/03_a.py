# Day 03: Rucksack Reorganization

# Read in rucksack files. Each line is a rucksack with two compartments.
# Find the common character between the two compartments.
# 
import sys
inputfile = sys.argv[1]
prioritytotal = 0

def checkrucks(ruckA, ruckB):
    for l in ruckA:
            if l in ruckB:
                return(l)

def priorityvalue(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38

with open(inputfile, "r") as file:
    for row in file:
        # strip and find middle
        ruck = row.strip()
        capacity = int(len(ruck) / 2)
        ruckA = ruck[0:capacity]
        ruckB = ruck[capacity:]
        prioritytotal += priorityvalue(checkrucks(ruckA, ruckB))

print(prioritytotal)



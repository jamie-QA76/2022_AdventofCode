# Day 03: Rucksack Reorganization, part 2

# Read in rucksack files. Every three lines is a group of elves.
# Find the character common to each set of three lines and return the value


import sys
inputfile = sys.argv[1]
prioritytotal = 0

def checkrucks(ruckA, ruckB, ruckC):
    for l in ruckA:
            if l in ruckB:
                if l in ruckC:
                    return(l)

def priorityvalue(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38

rucks = []

with open(inputfile, "r") as file:
    for row in file:
        rucks.append(row.strip())


totalgroups = int(len(rucks)/3)

for x in range(totalgroups):
    iteration = (x-1) * 3
    prioritytotal += priorityvalue(checkrucks(rucks[iteration], rucks[iteration+1], rucks[iteration+2]))

print(prioritytotal)



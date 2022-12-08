# Day 4: Camp cleanup

# Each line has a pair of ranges
# Check each pair to see if one range encompasses the other

import sys

inputfile = sys.argv[1]

paircount = 0

def compareranges(set):
    setA = set[0].split("-")
    setA = [int(i) for i in setA]
    setB = set[1].split("-")
    setB = [int(i) for i in setB]
    if setA[0] == setB[0]:
        return True
    elif setA[1] == setB[1]:
        return True
    elif (setA[0] < setB[0]) and (setA[1] > setB[1]):
        return True
    elif (setA[0] > setB[0]) and (setA[1] < setB[1]):
        return True
    else:
        return False


with open(inputfile, "r") as file:
    for row in file:
        set = row.strip().split(",")
        if compareranges(set):
            paircount += 1
        
print(str(paircount))
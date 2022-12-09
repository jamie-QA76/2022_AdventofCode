# Day 6: Tuning Trouble - Looping instead of regex

import sys

def countdown(n):
    for x in range(n-limit+1):
        dupes = 0
        segment = a[x:x+limit]
        for s in segment:
            if segment.count(s) > 1:
                dupes += 1
        if dupes == 0:
            return x + 14

inputfile = sys.argv[1]

file = open(inputfile, 'r')
a = file.read()
limit = 14

length = len(a)
start = countdown(length)

print(str(start))
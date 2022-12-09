# Day 6: Tuning Trouble

import sys
import re

inputfile = sys.argv[1]

file = open(inputfile, 'r')

a = file.read()

m = re.search(r'(.)(?!\1)(.)(?!(\1)|(\2))(.)(?!(\1)|(\2)|(\5))(.)', a)

print(m.group(0))
print(m.end(0))


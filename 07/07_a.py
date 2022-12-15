# Day 7: No Space Left On Device
import re
import sys

class TreeNode:
    def __init__(self, value, prev):
        self.value = value # data
        self.children = [] # references to other nodes
        self.size = 0
        self.parent = prev

    def add_child(self, child_node):
        # creates parent-child relationship
        # print("Adding " + child_node.value)
        self.children.append(child_node) 
    
    def remove_child(self, child_node):
        # removes parent-child relationship
        # print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]

    def update_size(self, filesize):
        self.size += filesize

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            previous_node = current_node.parent
            if previous_node == "":
                print("Current: ", current_node.value, "Size: ", str(current_node.size))
            else:
                print("Current: ", current_node.value, "Parent: ", previous_node.value, "Size: ", str(current_node.size))
            nodes_to_visit += current_node.children
    
    def compute_total(self):
        total_amount = self.size
        for x in self.children:
            total_amount += x.compute_total()
        results.append([self.value, total_amount])
        return total_amount
        


inputfile = sys.argv[1]
file = open(inputfile, 'r')
history = file.readlines()
counter = 0

for x in history:
    Cdir = re.match(r'dir (.*)\n', x)
    command = re.match(r'..(cd).(.+)\n', x)
    file = re.match(r'(\d+).*', x)
    if command:
        cname = command.group(2)
        if cname == "/":
            root = TreeNode(cname, None)
            current = root
            current.parent = ""
        elif cname != "..": #actual new directory
            nextdir = None
            for a in range(len(current.children)):
                if current.children[a].value == cname:
                    nextdir = a
            current = current.children[nextdir]
        elif cname == "..":
            # print(".. change", current.value, current.parent.value)
            current = current.parent
    if Cdir:
        dirname = Cdir.group(1)
        current.add_child(TreeNode(dirname, current))
    if file:
        filecontents = int(file.group(1))
        # print(current.value, file.group(1))
        current.update_size(filecontents)
    counter += 1


#root.traverse()
results = []
total_amount = root.compute_total()
final_amount = 0
for r in results:
    print(r)
    if r[1] <= 100000:
        final_amount += r[1]

print(str(final_amount))
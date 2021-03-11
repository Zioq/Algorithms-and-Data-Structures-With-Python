from datetime import datetime
from bst_structure import Node, BSTDemo

tree = BSTDemo()

# Open the txt tile
with open("data.txt") as f:
    for line in f:
        tree.insert(line)

tree.in_order()
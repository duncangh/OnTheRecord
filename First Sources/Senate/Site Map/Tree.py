# Binary Search Tree in Python

class Node:

    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChile = None

    def insert(self, data):

        # Check to see if this data is alread in the node
        if self.value == data:
            return False
        elif self.value > data:
            # Check to see if there is a leftChild
            if self.leftChild:
                return self.leftChild.insert(data)


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)

        # If the root node does not exist, create a new node and return True
        else:
            self.root = Node(data)
            return True
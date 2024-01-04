# Full tree 
# A tree where every node has either one or two children

# Complete tree
# A tree where every parent node is FILLED

# Root
# The node of the tree without any parents

# Leaf
# Any node of the tree without any children

# Binary Search Tree
# Any node to the ride of the root will be greater than, and the left will be less than

# Big O 
# O(log n)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
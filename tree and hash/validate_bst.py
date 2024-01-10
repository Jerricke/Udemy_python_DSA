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

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)          
        traverse(self.root)
        return results
        
    def is_valid_bst(self):
        nums = self.dfs_in_order()
        
        count = 0
        for _ in range(len(nums)-1):
            if nums[count + 1] < nums[count]:
                return False
            count += 1
        return True
            
    def is_valid_bst_solution(self):
        node_values = self.dfs_in_order()
        for i in range(1, len(node_values)):
            if node_values[i] <= node_values[i-1]:
                return False
        return True
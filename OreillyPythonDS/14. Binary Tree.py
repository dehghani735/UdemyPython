class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value: 
            self.left = self.addToSubTree(self.left, value)
        elif value > self.value:
            self.right = self.addToSubTree(self.right, value)

    def addToSubTree(self, parent, value):
        if parent is None:
            return BinaryNode(value)
        
        parent.add(value)
        return parent
    """two functions above are called double recursion"""

    def remove(self, value):
        if value < self.value:
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            if self.left is None:
                return self.right
            
            # find largest value in left subtree
            child = self.left
            while child.right:
                child = child.right

            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey
        
        return self
    
    def removeFromParent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        
        return False

b = BinaryTree()
b.add(7)
print(b.root.value)

print(7 in b)
print(1 in b)

b.add(1)

print(1 in b)

b.remove(1)

print(1 in b)
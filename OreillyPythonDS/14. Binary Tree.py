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

    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v
            
        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def getMin(self):
        if self.root is None:
            return ValueError("Binary Tree is Empty")

        n = self.root
        while n.left:
            n = n.left
        return n.value
    
    def getMax(self):
        if self.root is None:
            return ValueError("Binary Tree is Empty")

        n = self.root
        while n.right:
            n = n.right
        return n.value

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def closest(self, target):
        if self.root is None:
            return None
        
        node = self.root
        best = node
        distance = abs(self.root.value - target)
        while node:
            if abs(node.value - target) < distance:
                best = node
                distance = abs(node.value - target)
            
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return target
        
        return best.value

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

    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v

b = BinaryTree()
b.add(7)
print(b.root.value)

print(7 in b)
print(1 in b)

b.add(1)

print(1 in b)

b.remove(1)

print(1 in b)

print(b.getMax())

print(b.getMin())

print('*' * 10)

c = BinaryTree()
c.add(5)
c.add(2)
c.add(9)

print(5 in c)

print(c.closest(4))

c.add(-10)

print(c.closest(-20))

print('*' * 10)

d = BinaryTree()

d.add(10)
d.add(2)
d.add(6)
d.add(3)
d.add(7)

for _ in d:
    print(_)
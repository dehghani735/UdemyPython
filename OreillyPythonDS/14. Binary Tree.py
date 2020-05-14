class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.numLeft = 0

    def adjustCount(self, value, delta):
        """Adjust numLeft count after value has been added"""
        if value <= self.value:
            self.numLeft += delta
            if self.left:
                self.left.adjustCount(value, delta)
        elif value > self.value:
            if self.right:
                self.right.adjustCount(value, delta)

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
            self.numLeft -= 1
        
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
    def __init__(self, *start):
        self.root = None

        for _ in start:
            self.add(_)
    
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
        """
        Insert value into proper location in Binary Search Tree. Maintains Set Semantics.
        """
        if self.root is None:
            self.root = BinaryNode(value)
            return True
        else:
            # this check is for set semantics
            if value in self:
                return False
            
            ret = self.root.add(value)    
            self.root.adjustCount(value, +1)
    
    def remove(self, value):
        """
        Remove value from tree. Check if contained, first be attempting to remove, so we can update properly
        """
        if value in self:
            self.root = self.root.remove(value)
            self.root.adjustCount(value, -1)

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
    
    def Smallest(self, k):
        """
        Return kth smallest element in tree. If k greater than any of elements, return max. If smaller than 0, return min
        """
        if self.root is None:
            raise ValueError("Binary Tree is Empty")
        if k < 0:
            k = 0
        n = self.root
        while n:
            if n.numLeft == k:
                return n.value
            elif k < n.numLeft:
                n = n.left
            else:
                k = k - n.numLeft - 1 # adjust it so numLeft numbers are gone
                if n.right is None:
                    return n.value
                n = n.right

    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v

    def __repr__(self):
        if self.root is None:
            return "binary:()"
        return "binary:" +  str(self.root)

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

print('*' * 10)

e = BinaryTree(1,4,2,3,9,8,7,6,5)

print(e)

for _ in e:
    print(_)

print("Smallest: " + str(e.Smallest(0)))
print("Largest: " + str(e.Smallest(1000)))
print("First smallest one: " + str(e.Smallest(1)))  ## It has bug (fix it later)
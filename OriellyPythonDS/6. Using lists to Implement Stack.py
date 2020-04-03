class Stack:
    def __init__(self):
        self.__stack = []
    
    def isEmpty(self):
        return len(self.__stack) == 0
    
    def push(self, v):
        self.__stack.append(v)
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty.')
        return self.__stack.pop()
    
    def __repr__(self):
        #Show Representation
        return "stack:" + str(self.__stack)

s = Stack()
s.push(4)
s.push(5)
print(s)
s.pop()
print(s)
s.pop()
print(s)

print(s)
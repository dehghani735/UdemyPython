class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

class LinkedList:
    def __init__(self, *start):
        self.head = None

        for _ in start:
            self.prepend(_)
    
    def prepend(self, value):
        """Add value to front of the list"""
        self.head = LinkedNode(value, self.head)
    
    def remove(self, value):
        n = self.head
        last = None
        while n != None:
            if n.value == value:
                if last is None:
                    self.head = self.head.next
                else:
                    last.next = n.next
                return True
            
            last = n
            n = n.next
        return False

    def pop(self):
        """remove first value from list"""
        if self.head is None:
            raise Exception('Empty List.')
        val = self.head.value
        self.head = self.head.next
        return val

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head is None:
            return 'link:[]'

        return 'link:[{0:s}]'.format(','.join(map(str, self)))
    

a = LinkedList()
a.prepend(1)
a.prepend(2)
a.prepend(3)

print(a)

a.remove(2)

print(a)

#for _ in a:
#    print(_)
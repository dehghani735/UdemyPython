class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail

class QueueLinkedList:
    def __init__(self, *start):
        self.head = None
        self.tail = None

        for _ in start:
            self.add(_)
    
    def append(self, value):
        """Add value to end of queue"""
        newNode = LinkedNode(value, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def isEmpty(self):
        """Determine is Queue is Empty"""
        return self.head == None

    def pop(self):
        """remove first value from queue"""
        if self.head is None:
            raise Exception('Empty List.')
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def __iter__(self):
        """Iterator of values in queue"""
        n = self.head
        while n != None:
            yield n.value
            n = n.next
    
    def __repr__(self):
        if self.head is None:
            return 'queue:[]'

        return 'queue:[{0:s}]'.format(','.join(map(str, self)))
    
q = QueueLinkedList()
q.append(1)
q.append(2)
q.append(3)

print(q)

a = q.pop()

print(q)
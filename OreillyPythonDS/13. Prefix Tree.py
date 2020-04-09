"""990121"""

wordkey = '\n' # any character not 'a' .. 'z'

class PrefixTree:
    def __init__(self):
        self.head = {}
    
    def add(self, value):
        """Add value to Prefix Tree. Return True if updated"""
        d = self.head

        while len(value) > 0:
            c = value[0]
            if c not in d:
                d[c] = {}
            
            d = d[c]
            value = value[1:]
        
        if wordkey in d:
            return False
        
        d[wordkey] = True
        return True

    """Python has a really nice ability to use iterators for collections"""
    def __contains__(self, value):
        """VERY IMPORTANT"""
        """determine if value in prefix tree. It is used when 'in' command is executed."""
        d = self.head
        while len(value) > 0:
            c = value[0]
            if c not in d:
                return False
            d = d[c]
            value = value[1:]
        
        return wordkey in d

d = PrefixTree()
print(d.add('in'))
print(d)
print(d.add('inch'))
print(d)
print(d.add('inch'))

print('str' in d)

print('in' in d)

print('inc' in d)

print('inch' in d) 
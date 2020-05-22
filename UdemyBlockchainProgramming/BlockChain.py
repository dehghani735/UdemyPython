#BlockChain.py

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
# digest.update(b"abc")
# digest.update(b"123")
# hash = digest.finalize()
# print(hash)

# digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
# digest.update(b"abc")
# digest.update(b"124")
# hash = digest.finalize()
# print(hash)

class CBlock:
    data = None
    previousHash = None

    def __init__(self, data, previousBlock):
        pass

    def computeHash(self):
        return b'aaa'

if __name__ == '__main__':
    root = CBlock('I am root', Note)
    B1 = CBlock('I am a child.', root)
    B2 = CBlock('I am B1s brother', root)
    B3 = CBlock(2343, B1)
    B4 = CBlock(someClass('Hi there!'), B2)

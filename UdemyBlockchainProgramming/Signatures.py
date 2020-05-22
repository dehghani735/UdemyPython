#Signatures.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public = private.public_key()
    return private, public

def sign(message, private):
    message = bytes(str(message), 'utf-8')
    sig = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return sig

def verify(message, sig, public):
    message = bytes(str(message), 'utf-8')
    try:
        public.verify(
            sig,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print('Error! Executing public_key.verify')
        return False

if __name__ == '__main__':
    pr, pu = generate_keys()
    print(pr)
    print(pu)
    message = "This is a secret message"
    sig = sign(message, pr)
    print(sig)
    correct = verify(message, sig, pu)

    print(correct)

    if correct:
        print("Success! Good sig")
    else:
        print("Error! signature is bad")

    # if we do it wrong, be an attacker

    pr2, pu2 = generate_keys()
    sig2 = sign(message, pr2) # attacker private key
    correct = verify(message, sig2, pu) # your public key, because he is mimicing you
    if correct:
        print('ERROR! Bad signature checks out')
    else:
        print('Success! Bad sig detected')

    badmess = message + "Q"
    correct = verify(badmess, sig, pu) # your public key, because he is mimicing you
    if correct:
        print('ERROR! Tampered checks out')
    else:
        print('Success! Tampering detected')

    print(type(b"message"))
    print(type("message"))
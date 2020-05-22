# Udemy Blockchain Programming

By God.

This readme file is written by Mohammad Reza Dehghani Tafti.

Contact me at dehghani735@gmail.com

Start Date: 13990225

---

## 2. Digital Signatures

### Whats a digital signature

- The key is that they are easy to verify, but hard to mimic
- Asymetric Encryption
  - RSA

### RSA

- RSA key gen ( begins by generating two keys)
  - public key: which can be shared with the whole world
  - private key: that you keep to yourself
- Example: online shopping, we want to send our credit card to online market; Internet is not a very secure channel. Vendor sends us its public key. you use that public key using the math involved in asymetric encryption to encrypt a message and send those over the internet to them. and the vendor using their private key can turn those random-looking bits back into your credit card number.

### Digital Signatures

- They work almost in reverse. (TODO فک کنم بعدا بفهمم دقیق چیه)

### Signatures for Cryptocurrencies

- The connection to cryptocurrencis is that the thing we'll be signing are entries in a public ledger. So when I want to send coins to someone else, I'll take the statement "Levi gives Andi 10 coins" and I'll use my private key to generate a signature for that message. So I'm gonna sign it and I'll get out these random bits.
- Now Andi's then gonna want to spend her coins. But in order to spend them, whoever she's giving the coins to needs to know that she actually owns them. This signature my signature on this statement "Levi gives Andi 10 coins" is the verificatin that she owns those coins.
- So already, as soon as we can create digital signatures, we have statements that we can sign that are verifiable easily that we can post to a public ledger. That ledger is eventually going to be a blockchain.
- Now we are gonna go about building a system to sign transations and verify them using Python.

### TDD

- write tests together
- you try on your own
- we solve it together

### Assignment

Signatures.py

sign function: In the context of encryption, what I'm really doing is taking this message and effectively decrypting it as if it were an encrypted message. That creates the signature.

verify function: verify the sig. Anyone with the public key can verify the signature.

### Strings or Bytes

- b"ali" means byte
- try type(b"message")
- encryption methods need to take byte messages instead of string
- Note: I can't encode sth that is already encoded.

## 3. Block Chain

### Hash Functions

- The blocks in our blockchain will be able to store any data that can be converted to a string and we'll be detect any tampering that's gone on.
- Hash Function: is an algorithm that converts a string of arbitrary length into a string of bits of a fixed length and it's got to do so in a predictable way.
- Hashs in CS to speed up certain algorithms; but a cryptographic hash has additional requirements.
  - First a cryptographic hash should be what we call **non-malleable**; two very similar inputs should not produce similar outputs. We want any slight change to be instantly visible.
  - to be **collision resistant**: since there are few hash values available, then the almost infinite number of messages we could throw into our hash, there are bound to be some collisions. but the collision resistance means that the only sensible way to find two inputs that produce the same output is to compute the hash of many many input functions until you stumble onto one; It shouldn't be easy to find this.
  - The hash function we'll use for our blockchain is the same one that we use for reducing the message size for our digital signatures: SHA-256

### Block Chains

- A blockchain is gonna consist of blocks and each of the blocks is going to contain some data and then also the hash of the block that preceded it. When i add a new hash with some new data, the hash will contain the data itself, and then I'll compute the hash of the previous block including of course its stored hash of the block before it. And I'll put that in as part of my block.
- The advantage is that tampering is always apparent very quickly. So if someone wanted to tamper with an earier block, and if our hash is a good one, then the modified data will cause the hash of the next block not to match with a recomputed hash of this block. and they don't match and so
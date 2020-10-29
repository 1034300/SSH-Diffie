# Diffie Hellman computations run in the same script.

import random

# D.H. parameters
g = 2
p = 65521

# Alice picks a random exponent a between 1 and p:
# (this is Alice's private number)
a = random.randint(1, p)

# Bob picks a random exponent b between 1 and p:
# (this is Bob's private number)
b = random.randint(1, p)

# Alice computes her public number A = g^a mod p:
A = g**a % p

# Bob computes his public number B = g^b mod p:
B = g**b % p

# Bob computes the shared secret, which is A^b (from his point of view)
shared_secret_Bobs_POV = A**b % p

# Alice computes the shared secret, which is B^a (from her point of view)
shared_secret_Alices_POV = B**a % p

print("a: ", a)
print("b: ", b)
print("A: ", A)
print("B: ", B)

print("A**b", shared_secret_Bobs_POV)
print("B**a", shared_secret_Alices_POV)

# This can be encrypted, but should be 
# in a proper format.
# Alternatively, use XOR encryption.
plaintext = str(67)
key = str(shared_secret_Bobs_POV)

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#key = os.urandom(32) # This generates a random key
iv = os.urandom(16) # IV is used when we transmit several AES blocks
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b"67") + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()
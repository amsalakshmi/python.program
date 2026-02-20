import random
from math import gcd

# Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate small prime number
def generate_prime():
    while True:
        num = random.randint(100, 300)
        if is_prime(num):
            return num

# Modular inverse (Extended Euclidean Algorithm)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

# Generate RSA keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Encrypt message
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt message
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)


# ---- Run Program ----
public_key, private_key = generate_keys()

print("🔑 Public Key:", public_key)
print("🔐 Private Key:", private_key)

message = input("Enter message: ")

encrypted = encrypt(message, public_key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, private_key)
print("Decrypted:", decrypted)
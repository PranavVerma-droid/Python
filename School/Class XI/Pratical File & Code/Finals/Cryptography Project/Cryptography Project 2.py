# This file contains the Final Version of my Cryptography Algorithm.
# ! STILL IN DEVELOPMENT
# Made by Pranav Verma, XI Raman.

"""
Basic Principle:

The Idea:
This program generates two sets of keys: a private key and a public key.
Imagine you want to send a message over the internet. Even if you delete the message, it can still be stored on a server.
You might think you could encrypt the message with just one key, but then how would you securely send the key to the recipient?
This is where the RSA Algorithm comes in.
My algorithm is a simplified version of the RSA Algorithm, which is widely used today for secure data transmission, such as in HTTPS protocols.

How to use this program:
1. Generate a pair of keys (public and private) using this program.
2. Share the public key with the person who wants to send you a secret message.
3. The sender will use the public key to encrypt their message using this program and send the encrypted message back to you.
4. Use your private key to decrypt the received message using this program.
5. If you want to send a message back, the sender can generate their own key pair and share their public key with you.

In summary, each party will have a pair of keys: a private key for decryption and a public key for encryption. This ensures secure message transmission.
"""

import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keys():
    primes = []
    for i in range(50, 101):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def encrypt_message(message, public_key):
    e, n = public_key
    encrypted_message = []
    for char in message:
        encrypted_char = (ord(char) ** e) % n
        encrypted_message.append(str(encrypted_char))
    return ' '.join(encrypted_message)

def decrypt_message(encrypted_message, private_key):
    d, n = private_key
    encrypted_chars = encrypted_message.split()
    decrypted_message = ''.join([chr((int(char) ** d) % n) for char in encrypted_chars])
    return decrypted_message


print("Welcome to the Public Key Message Encoder/Decoder!")

print("\nChoose an option:")
print("1. Encrypt a message")
print("2. Decrypt a message")
print("3. Generate keys")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    public_key_input = input("Enter your public key (e,n) separated by a comma: ")
    e, n = [int(x) for x in public_key_input.split(',')]
    public_key = (e, n)

    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt_message(message, public_key)
    print("Encrypted Message:", encrypted_message)

elif choice == "2":
    private_key_input = input("Enter your private key (d,n) separated by a comma: ")
    d, n = [int(x) for x in private_key_input.split(',')]
    private_key = (d, n)


    encrypted_message_input = input("Enter the encrypted message as space-separated numbers: ")
    decrypted_message = decrypt_message(encrypted_message_input, private_key)
    print("Decrypted Message:", decrypted_message)

elif choice == "3":
    public_key, private_key = generate_keys()
    print("New keys generated:")
    print("Public Key (e,n):", public_key)
    print("Private Key (d,n):", private_key)
    print("Try Rerunning the Program and Encrypting an Message.")

else:
    print("Please Enter 1, 2, or 3.")


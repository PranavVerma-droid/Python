# This file contains the Advanced Version of my Cryptography Project.
# Made by Pranav Verma.

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

def main():
    print("Welcome to the Public Key Message Encoder/Decoder!")

    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Generate keys")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        public_key_input = input("Enter your public key (e,n) separated by a comma: ")
        try:
            e, n = map(int, public_key_input.split(','))
            public_key = (e, n)
        except ValueError:
            print("Invalid key format. Please enter the key as comma-separated integers.")
            return

        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, public_key)
        print("Encrypted Message:", encrypted_message)

    elif choice == "2":
        private_key_input = input("Enter your private key (d,n) separated by a comma: ")
        try:
            d, n = map(int, private_key_input.split(','))
            private_key = (d, n)
        except ValueError:
            print("Invalid key format. Please enter the key as comma-separated integers.")
            return

        encrypted_message_input = input("Enter the encrypted message as space-separated numbers: ")
        decrypted_message = decrypt_message(encrypted_message_input, private_key)
        print("Decrypted Message:", decrypted_message)

    elif choice == "3":
        public_key, private_key = generate_keys()
        print("New keys generated:")
        print("Public Key (e,n):", public_key)
        print("Private Key (d,n):", private_key)

    else:
        print("Please Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
import random

def generate_keys():
    p = random.randint(50, 100)
    q = random.randint(50, 100)
    n = p * q

    e = random.randint(1, 100)
    d = random.randint(1, 100)

    return ((e, n), (d, n))

def encrypt_message(message, public_key):
    e, n = public_key
    encrypted_message = [(ord(char) + e) % 256 for char in message]
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr((char - d) % 256) for char in encrypted_message])
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
        d, n = map(int, private_key_input.split(','))
        private_key = (d, n)

        encrypted_message_input = input("Enter the encrypted message as comma-separated numbers: ")
        try:
            encrypted_message = [int(x) for x in encrypted_message_input.split(',')]
            decrypted_message = decrypt_message(encrypted_message, private_key)
            print("Decrypted Message:", decrypted_message)
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

    elif choice == "3":
        public_key, private_key = generate_keys()
        print("New keys generated:")
        print("Public Key (e,n):", public_key)
        print("Private Key (d,n):", private_key)

    else:
        print("Please Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
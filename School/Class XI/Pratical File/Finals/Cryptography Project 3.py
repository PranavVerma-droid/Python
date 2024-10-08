import random

def generate_keys():
    public_key = random.randint(1, 255)  # Ensure public key is within the range of 1 to 255
    private_key = 256 - public_key  # Simple relationship for modular inverse under 256
    print(f"Keys generated:\nPublic Key: {public_key}\nPrivate Key: {private_key}")

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    public_key = int(input("Enter the public key: "))
    encrypted_message = [(ord(char) + public_key) % 256 for char in message]
    print("Encrypted message:", ' '.join(map(str, encrypted_message)))

def decrypt_message():
    encrypted_message = list(map(int, input("Enter the encrypted message (space-separated integers): ").split()))
    private_key = int(input("Enter the private key: "))
    decrypted_message = ''.join(chr((char - private_key + 256) % 256) for char in encrypted_message)
    print("Decrypted message:", decrypted_message)

def main():
    print("1. Generate keys")
    print("2. Encrypt message")
    print("3. Decrypt message")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        generate_keys()
    elif choice == '2':
        encrypt_message()
    elif choice == '3':
        decrypt_message()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
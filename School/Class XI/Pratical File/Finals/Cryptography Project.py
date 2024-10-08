def encode_message(message, shift):
    encoded = ""
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Shift within the alphabet (upper and lower case separately)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain the same
            encoded += char
    return encoded


def decode_message(encoded_message, shift):
    # Decoding is just encoding with a negative shift
    return encode_message(encoded_message, -shift)


def main():
    print("Welcome to the Secret Message Encoder/Decoder!")
    print("Choose an option:")
    print("1. Encode a message")
    print("2. Decode a message")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        message = input("Enter the message to encode: ")
        shift = int(input("Enter the shift value (1-25): "))
        encoded_message = encode_message(message, shift)
        print("Encoded Message:", encoded_message)

    elif choice == "2":
        encoded_message = input("Enter the message to decode: ")
        shift = int(input("Enter the original shift value (1-25): "))
        decoded_message = decode_message(encoded_message, shift)
        print("Decoded Message:", decoded_message)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

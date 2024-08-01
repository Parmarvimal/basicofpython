def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Enter 'Q' to quit): ").upper()
        if choice == 'Q':
            break
        if choice not in ['E', 'D']:
            print("Invalid choice! Please enter 'E', 'D', or 'Q'.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()

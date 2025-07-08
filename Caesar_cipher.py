def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)


def main():
    print("Caesar Cipher Tool")
    choice = input("Choose an option (e=encrypt/d=decrypt): ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")


if __name__ == "__main__":
    main()

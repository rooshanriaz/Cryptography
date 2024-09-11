def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print(f"Encrypted: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted: {decrypted_text}")
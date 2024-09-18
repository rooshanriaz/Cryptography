from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Function to pad data to the AES block size (16 bytes)
def pad(data):
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length] * padding_length)

# Function to unpad the data after decryption
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# AES encryption
def encrypt(plaintext, key):
    iv = os.urandom(16)  # Generate a random initialization vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padded_data = pad(plaintext)
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext  # Return IV concatenated with ciphertext

# AES decryption
def decrypt(ciphertext, key):
    iv = ciphertext[:16]  # Extract IV from the first 16 bytes
    actual_ciphertext = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return unpad(padded_plaintext)

# Example usage
if __name__ == "__main__":
    key = os.urandom(32)  # AES-256 uses a 32-byte key
    plaintext = b"Hello, this is a block cipher example!"

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text.decode()}")

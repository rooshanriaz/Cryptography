from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Stream cipher encryption using RC4
def encrypt_stream_cipher(plaintext, key):
    # Create the RC4 cipher object
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext)
    return ciphertext

# Stream cipher decryption using RC4
def decrypt_stream_cipher(ciphertext, key):
    # Create the RC4 cipher object
    cipher = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    decrypted_text = decryptor.update(ciphertext)
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = os.urandom(16)  # RC4 key length can vary, here we're using 16 bytes
    plaintext = b"Stream cipher example!"

    # Encrypt the plaintext
    ciphertext = encrypt_stream_cipher(plaintext, key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_stream_cipher(ciphertext, key)
    print(f"Decrypted text: {decrypted_text.decode()}")

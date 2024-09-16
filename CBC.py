from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def cbc_encrypt(plain_text, key, iv):
    # Create a cipher object using CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad plaintext to be multiple of block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plain_text = padder.update(plain_text) + padder.finalize()
    
    # Encrypt the padded plaintext
    encrypted_text = encryptor.update(padded_plain_text) + encryptor.finalize()
    return encrypted_text

def cbc_decrypt(encrypted_text, key, iv):
    # Create a cipher object using CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the encrypted text
    padded_plain_text = decryptor.update(encrypted_text) + decryptor.finalize()
    
    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plain_text = unpadder.update(padded_plain_text) + unpadder.finalize()
    return plain_text

# Example usage
key = os.urandom(16)  # AES key should be either 16, 24, or 32 bytes long
iv = os.urandom(16)   # AES block size is 16 bytes
plain_text = b'This is a test message for CBC mode.'

encrypted_text = cbc_encrypt(plain_text, key, iv)
print(f'Encrypted (CBC): {encrypted_text}')

decrypted_text = cbc_decrypt(encrypted_text, key, iv)
print(f'Decrypted (CBC): {decrypted_text}')

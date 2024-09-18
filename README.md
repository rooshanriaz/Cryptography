# Cryptography Algorithms

This repository contains implementations of various cryptographic algorithms that I am studying in my university cryptography course. The goal is to provide a clear and concise implementation of each algorithm along with explanations of how they work.

## Table of Contents
- [Implemented Algorithms](#implemented-algorithms)
  - [Caesar Cipher](#caesar-cipher)
  - [Transposition Cipher](#transposition-cipher)
  - [Vernam Cipher](#vernam-cipher)
    - [Method](#method)
  - [Block Cipher](#block-cipher)
  - [Stream Cipher](#stream-cipher)
  - [ECB Mode of Operation](#ecb-mode-of-operation)
  - [CBC Mode of Operation](#cbc-mode-of-operation)
 - [Usage](#usage)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Implemented Algorithms

### Caesar Cipher
The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

You can find the implementation of the Caesar Cipher in the `caesar_cipher.py` file.

### Transposition Cipher
The Transposition Cipher works by rearranging the characters of the plaintext according to a specific system. In this implementation, a columnar transposition cipher is used.

You can find the implementation of the Transposition Cipher in the `transposition_cipher.py` file.

### Vernam Cipher

Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting plain text into cipher text. In this mechanism, we assign a number to each character of the Plain-Text, like (a = 0, b = 1, c = 2, … z = 25). 

#### Method

Bitwise XOR both the number (Corresponding plain-text character number and Key character number). 
Subtract the number from 26 if the resulting number is greater than or equal to 26, if it isn’t then leave it.

### Block Cipher

A Block Cipher encrypts data in fixed-size blocks, typically 64 or 128 bits. It processes each block of data separately and uses the same key for each block. Padding is added to the last block if the data is not a multiple of the block size. Common block ciphers include AES and DES. Block ciphers are well-suited for scenarios requiring secure encryption of large data sets, such as file encryption. Block ciphers work best for large data.

### Stream Cipher

A Stream Cipher encrypts data one bit or byte at a time, often using a key stream generated from a secret key. Stream ciphers are faster than block ciphers and do not require padding. They are often used for encrypting real-time data such as voice or video streams. A popular example of a stream cipher is RC4, though more modern ciphers like ChaCha20 offer better security. Stream ciphers excel in fast, continuous data streams.

### ECB Mode of Operation

Electronic Codebook (ECB) mode is the simplest form of encryption where each block of plaintext is encrypted independently using the same key.

### CBC Mode of Operation

Cipher Block Chaining (CBC) mode uses an initialization vector (IV) and chains the encryption of each block with the previous block.

#### Usage:
1. Clone the repository:
    ```bash
    git clone https://github.com/rooshanriaz/Cryptography-CY-312.git
    ```
2. Navigate to the folder containing the implementation.
3. Run the scripts:
    ```bash
    python caesar_cipher.py
    python transposition_cipher.py
    python vernam-cipher.py
    python block-cipher.py
    pytohn stream-cipher.py
    python ECB.py
    python CBC.py
    ```

## How to Use
Each algorithm is implemented as a standalone Python script. You can run them individually by following the instructions provided in the corresponding script files. 

## Contributing
Feel free to fork the repository, create a branch, and make contributions or improvements to the code.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

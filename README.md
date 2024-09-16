# Cryptography Algorithms

This repository contains implementations of various cryptographic algorithms that I am studying in my university cryptography course. The goal is to provide a clear and concise implementation of each algorithm along with explanations of how they work.

## Table of Contents
- [Implemented Algorithms](#implemented-algorithms)
  - [Caesar Cipher](#caesar-cipher)
  - [Transposition Cipher](#transposition-cipher)
  - [Vernam Cipher](#vernam-cipher)
    - [Method](#method)
  - [ECB Mode](#ecb-mode)
  - [CBC Mode](#cbc-mode)
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

#### Usage:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cryptography-algorithms.git
    ```
2. Navigate to the folder containing the implementation.
3. Run the scripts:
    ```bash
    python caesar_cipher.py
    python transposition_cipher.py
    python vernam-cipher.py
    ```

## How to Use
Each algorithm is implemented as a standalone Python script. You can run them individually by following the instructions provided in the corresponding script files. 

## Contributing
Feel free to fork the repository, create a branch, and make contributions or improvements to the code.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

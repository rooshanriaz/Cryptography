import math

def encrypt_message(key, message):
    # Create an empty list to store the ciphertext
    ciphertext = [''] * key

    # Loop through each column in the ciphertext
    for column in range(key):
        current_index = column

        # Keep adding characters from the message in the current column
        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    # Convert the ciphertext list into a single string and return it
    return ''.join(ciphertext)

def decrypt_message(key, message):
    # Calculate the number of columns
    num_columns = math.ceil(len(message) / key)
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(message)

    # Create an empty list to store the plaintext
    plaintext = [''] * num_columns

    column = 0
    row = 0

    # Loop through each character in the message
    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Move to the next column

        # If there are no more columns or we are at a shaded box, move to the next row
        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - num_shaded_boxes):
            column = 0
            row += 1

    # Convert the plaintext list into a single string and return it
    return ''.join(plaintext)


# Example usage
key = 5
message = "Hello, this is a transposition cipher"

encrypted = encrypt_message(key, message)
print("Encrypted:", encrypted)

decrypted = decrypt_message(key, encrypted)
print("Decrypted:", decrypted)

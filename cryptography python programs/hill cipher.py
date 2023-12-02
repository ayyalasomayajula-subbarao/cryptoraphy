import numpy as np

def prepare_text(text, block_size):
    text = text.replace(" ", "").upper()
    # Pad the text with 'X' to make its length a multiple of block_size
    if len(text) % block_size != 0:
        text += 'X' * (block_size - len(text) % block_size)
    return text

def text_to_matrix(text, block_size):
    matrix = []
    for i in range(0, len(text), block_size):
        matrix.append([ord(char) - ord('A') for char in text[i:i+block_size]])
    return np.array(matrix)

def matrix_to_text(matrix):
    return ''.join([chr(value % 26 + ord('A')) for row in matrix for value in row])

def hill_cipher(plaintext, key_matrix):
    plaintext = prepare_text(plaintext, len(key_matrix))
    plaintext_matrix = text_to_matrix(plaintext, len(key_matrix))
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    return matrix_to_text(ciphertext_matrix)

# Step 1: Read plain text from the user
plaintext = input("Enter the plain text: ")

# Step 2: Read the key matrix from the user
key_str = input("Enter the key matrix (row-wise, space-separated): ")
key_matrix = np.array([list(map(int, row.split())) for row in key_str.split()])

# Step 3: Encrypt the plain text
ciphered_text = hill_cipher(plaintext, key_matrix)

# Step 4: Display the obtained cipher text
print("Original Text:", plaintext)
print("Ciphered Text:", ciphered_text)

def prepare_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    return text

def generate_key_matrix(keyword):
    keyword = prepare_text(keyword)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []

    # Create a list with the unique characters of the keyword
    key_list = list(dict.fromkeys(keyword))

    # Fill in the remaining cells with the alphabet (excluding 'J')
    for char in alphabet:
        if char not in key_list and char != 'J':
            key_list.append(char)

    # Convert the list to a 5x5 matrix
    for i in range(0, 25, 5):
        key_matrix.append(key_list[i:i+5])

    return key_matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_cipher(plaintext, key_matrix):
    plaintext = prepare_text(plaintext)
    # Add a dummy character if the length is odd
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]

        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)

        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext

# Step 1: Read plain text from the user
plaintext = input("Enter the plain text: ")

# Step 2: Read keyword from the user
keyword = input("Enter the keyword: ")

# Step 3: Generate key matrix
key_matrix = generate_key_matrix(keyword)

# Step 4: Encrypt the plain text
ciphertext = playfair_cipher(plaintext, key_matrix)

# Step 5: Display the obtained cipher text
print("Ciphered Text:", ciphertext)

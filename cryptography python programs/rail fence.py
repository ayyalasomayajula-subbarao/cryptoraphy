def encrypt_rail_fence(plaintext, key):
    fence = [''] * key
    direction = 1

    row = 0
    for char in plaintext:
        fence[row] += char
        row += direction

        if row == key - 1 or row == 0:
            direction = -direction

    return ''.join(fence)

def decrypt_rail_fence(ciphertext, key):
    fence = [''] * key
    direction = 1

    index = 0
    for i in range(len(ciphertext)):
        fence[index] += 'X'
        index += direction

        if index == key - 1 or index == 0:
            direction = -direction

    fence[0] = ciphertext

    fence_text = ''.join(fence)
    decrypted_text = ''
    direction = 1
    index = 0

    for char in ciphertext:
        if char.isalpha():
            decrypted_text += fence_text[index]
            index += direction

            if index == len(fence_text) - 1 or index == 0:
                direction = -direction

    return decrypted_text

# Step 1: Read input text from the user
input_text = input("Enter the input text: ")

# Step 2: Encrypt the input text using Rail Fence Cipher
key = len(input_text) // 2  # Set the key based on the length of the input text
encrypted_text = encrypt_rail_fence(input_text, key)

# Step 3: Display the obtained encrypted text
print("Encrypted Text:", encrypted_text)

# Step 4: Decrypt the encrypted text using Rail Fence Cipher
decrypted_text = decrypt_rail_fence(encrypted_text, key)

# Step 5: Display the obtained decrypted text
print("Decrypted Text:", decrypted_text)

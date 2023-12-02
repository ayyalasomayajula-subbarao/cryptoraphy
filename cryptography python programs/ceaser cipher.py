def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_code = ord(char)
            shifted_code = (ascii_code - ord('A' if is_upper else 'a') + shift) % 26
            result += chr(shifted_code + ord('A' if is_upper else 'a'))
        else:
            result += char

    return result

# Step 1: Read plain text from the user
plaintext = input("Enter the plain text: ")

# Step 2: Read shift value from the user
shift_value = int(input("Enter the shift value: "))

# Step 3: Encrypt the plain text
ciphered_text = caesar_cipher(plaintext, shift_value)

# Step 4: Display the obtained cipher text
print("Original Text:", plaintext)
print("Ciphered Text:", ciphered_text)

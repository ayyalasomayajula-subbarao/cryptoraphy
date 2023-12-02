def vigenere_cipher(text, key, mode='encipher'):
    result = ''
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % len(key)].upper()) - 65
            if mode == 'decipher':
                shift = -shift
            result += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def main():
    while True:
        print("\n1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = input("\nEnter Your Choice: ")
        if choice == '3':
            break
        elif choice == '1':
            text = input("\nEnter Plain Text: ")
            key = input("Enter Key Value: ")
            result = vigenere_cipher(text, key)
            print("\nResultant Cipher Text:", result)
        elif choice == '2':
            text = input("\nEnter Cipher Text: ")
            key = input("Enter Key Value: ")
            result = vigenere_cipher(text, key, 'decipher')
            print("\nResultant Plain Text:", result)
        else:
            print("Please Enter Valid Option.")

if __name__ == "__main__":
    main()

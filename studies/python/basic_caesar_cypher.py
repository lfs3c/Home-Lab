# Caesar Cipher - Simple Implementation

# Character sets
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
num_letters = len(lowercase_letters)  # both have same length

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':   # decrypt
        key = -key

    for letter in text:
        if letter == ' ':
            result += ' '
        else:
            # choose which set to use
            if letter.islower():
                letters = lowercase_letters
            else:
                letters = uppercase_letters

            index = letters.find(letter)
            if index == -1: 
                result += letter
            else:
                new_index = index + key
                # wrap around
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters

                if letter.islower():
                    result += lowercase_letters[new_index]
                else:
                    result += uppercase_letters[new_index]

    return result


# Main program
print("\n*** Caesar Cipher Program ***\n")
user_input = input("Do you want to encrypt or decrypt? (e/d): ")

if user_input == 'e':
    print("\nEncrypting...\n")
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f"\nEncrypted text: {ciphertext}")

elif user_input == 'd':
    print("\nDecrypting...\n")
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f"\nDecrypted text: {plaintext}")

else:
    print("Invalid option. Please choose 'e' or 'd'.")

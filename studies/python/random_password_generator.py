#This Python program generates a random password following specific security rules. 
#The password has a random length between 8 and 16 characters, and each character is randomly selected from the 
#printable ASCII range (positions 33 to 126). It uses the chr() and random.randint() functions to build the password 
#and returns it as a single string.

import random  # Importing the random module

# Function that generates and returns a random password
def PsswrdGenerate():
    # Generate a random password length between 8 and 16 characters (inclusive)
    passwordLength = random.randint(8, 16)

    # Create a random password using characters from ASCII 33 to 126
    # "_" is a throwaway variable (its value is intentionally ignored)
    # random.randint(33, 126) picks a random ASCII code
    # chr() converts that code into its corresponding character
    # The for-loop runs "passwordLength" times to build the password
    # ''.join() concatenates all generated characters into a single string
    password = ''.join(chr(random.randint(33, 126)) for _ in range(passwordLength))

    # Display the generated password
    print("Generated Password:", password)

    # Return the password (optional, for reuse)
    return password


# Call the function
PsswrdGenerate()

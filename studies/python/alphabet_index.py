#This Python program asks the user to enter a number and returns the corresponding letter 
#in the English alphabet. It demonstrates basic string indexing and user input handling. 
#The program helps students practice how to access characters in a string using numeric positions.


alphabet = 'abcdefghijklmnopqrstuvwxyz' #Variable provided by Professor

while True: #begin the loop
  #ask user to enter a number between 1 and 26
  number = int(input("Please enter a number (1 - 26) to find out the corresponding letter in the alphabet: "))

  #check if variable is between 1 and 26
  if number > 0 and number < 27:

    #Select the digit of string wich number correspond with user input number
    letter = alphabet[number - 1]
    print("The number you have entered: ", number, "represents the letter:", letter)
    break #breaks the loop
  else:
    print("Sorry, your number:", number, "is not between 1 and 26, try again.")

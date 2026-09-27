#This Python program simulates rolling a pair of dice using the random module.
#Each die roll is generated using the random.randrange() function inside a custom roll_die() function.
#The main program calls this function twice, displays both individual rolls, and prints the total.

import random  # Importing the random module

# Function to simulate rolling one die
def roll_die():
    # Generate and return a random number between 1 and 6
    roll = random.randrange(1, 7)
    return roll

# Main function
def main():
    # Roll two dice using the roll_die() function
    die1 = roll_die()
    die2 = roll_die()

    # Calculate the total
    total = die1 + die2

    # Display results
    print("Die 1 rolled:", die1)
    print("Die 2 rolled:", die2)
    print("The total of both dice is:", total)

# Execute the program
main()

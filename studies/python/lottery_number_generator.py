# Description:
# Generates a seven-digit lottery number using random numbers from 0–9,
# and displays them in a list. Also includes an extra credit version that
# simulates Mega Millions rules: 6 unique numbers from 1–70 plus a Mega Ball (1–25).

import random  # Importing the random module

# ------------------------------------------------------------
# Part 1 – Generate a 7-digit lottery number (digits 0–9)
# ------------------------------------------------------------

def generate_lottery_numbers():
    """Generate a list with 7 unique random digits between 0 and 9."""
    lottery_numbers = []

    # Keep adding until we have 7 unique digits
    while len(lottery_numbers) < 7:
        new_number = random.randint(0, 9)
        if new_number not in lottery_numbers:
            lottery_numbers.append(new_number)

    return lottery_numbers


def display_lottery_numbers(numbers):
    """Print the generated 7-digit lottery number list."""
    print("Lottery Number (7 digits):", numbers)


def main_lottery():
    """Main function for the standard 7-digit lottery."""
    numbers = generate_lottery_numbers()
    display_lottery_numbers(numbers)



# Mega Millions Version
def generate_mega_millions():
    """
    Generate six unique numbers from 1 to 70
    and one 'Mega Ball' number from 1 to 25.
    """
    mega_numbers = random.sample(range(1, 71), 6)  # ensures unique numbers
    mega_ball = random.randint(1, 25)

    # Display the results
    print("\nMega Millions Numbers (1–70):", mega_numbers)
    print("Mega Ball (1–25):", mega_ball)


def main():
    """Main controller – runs both versions."""
    print("=== Lottery Number Generator ===")
    main_lottery()

    print("\n=== Mega Millions ===")
    generate_mega_millions()



# Program Execution
if __name__ == "__main__":
    main()

# Description:
# Prompts the user for two numbers (dividend and divisor),
# validates that the dividend is between 1 and 100,
# and handles division by zero errors using exception handling.

def get_valid_dividend():
    """Prompt user until a valid dividend between 1 and 100 is entered."""
    while True:
        try:
            dividend = int(input('Enter a whole number between 1 and 100: '))
            if 1 <= dividend <= 100:
                return dividend
            else:
                print('Number must be between 1 and 100. Try again.')
        except ValueError:
            print('Invalid input. Please enter a whole number.')

def main():
    print('\nThis program divides two numbers safely.')
    print('First, enter a dividend between 1 and 100.')
    dividend = get_valid_dividend()

    while True:
        try:
            divisor = int(input('Enter a divisor (cannot be zero): '))
            quotient = dividend / divisor
            print(f'\nResult: {dividend} divided by {divisor} equals {quotient:.4f}')
            break
        except ValueError:
            print('Invalid input. Please enter a whole number.')
        except ZeroDivisionError:
            print('Division by zero is not allowed. Please try again.')

if __name__ == "__main__":
    main()

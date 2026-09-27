# Description:
# Writes the numbers 1 through 100 into a text file named
# "numbers.txt", placing each number on a separate line.

def main():
    filename = "numbers.txt"

    try:
        with open(filename, 'w') as file:
            for number in range(1, 101):
                file.write(str(number) + '\n')

        print(f'Success! Numbers 1 through 100 have been written to "{filename}".')

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()

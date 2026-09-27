# Description:
# Reads the contents of a text file and counts the number of times each
# word appears. The program stores results in a dictionary, where each
# key is a word and each value is the frequency of that word.
# The results are then displayed in alphabetical order.

# Ask user for the file name (must include extension, e.g. "text1.txt")
file_name = input("Enter the name of the text file (example: text1.txt):\n")

# Create an empty dictionary to hold word counts
word_counts = {}

def main():
    """Main function that reads a text file and counts word frequency."""
    try:
        # Open the file for reading
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read each line in the file
            for each_line in file:
                # Convert line to lowercase for consistent counting
                each_line = each_line.lower()

                # Split line into words
                words = each_line.split()

                # Process each word
                for word in words:
                    # Remove punctuation from the word
                    word = word.strip('!"#$%&()*+,-./:;<=>?@\\[]^_{|}~`')

                    # Count occurrences
                    if word in word_counts:
                        word_counts[word] += 1  # Increment count if word exists
                    else:
                        word_counts[word] = 1   # Add new word with count 1

        # Display results
        print("\nWord Frequencies:\n")
        # Sort dictionary by word (key) and display results line by line
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")


# Run the program
if __name__ == '__main__':
    main()

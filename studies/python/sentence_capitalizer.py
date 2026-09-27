# Description:
# Accepts a string input from the user and returns a version
# of the text where the first character of each sentence is capitalized.
# For example: "hello. my name is Joe." → "Hello. My name is Joe."

# Function to capitalize the first character of each sentence
def capitalize_sentences(my_string):
    """
    Receives a string and returns it with each sentence capitalized.
    Sentences are assumed to end with '.', '!' or '?'.
    """
    # Split the text by period, question mark, or exclamation
    import re
    sentences = re.split(r'([.!?])', my_string)

    # Capitalize first letter of each sentence and rebuild the string
    capitalized = ""
    for i in range(0, len(sentences) - 1, 2):
        sentence = sentences[i].strip().capitalize()
        punctuation = sentences[i + 1]
        capitalized += sentence + punctuation + " "

    # Handle case with no punctuation at the end
    if len(sentences) % 2 != 0 and sentences[-1].strip():
        capitalized += sentences[-1].strip().capitalize()

    return capitalized.strip()


# Main function to get user input and display result
def main():
    while True:
        # Ask the user to input a sentence
        my_string = input("Please enter a sentence or paragraph:\n").strip()

        if len(my_string) < 1:
            print("Sorry, you entered an empty value. Please try again.\n")
        else:
            # Call the function and print the formatted result
            result = capitalize_sentences(my_string)
            print("\nCapitalized text:")
            print(result)
            break


# Program execution
if __name__ == "__main__":
    main()

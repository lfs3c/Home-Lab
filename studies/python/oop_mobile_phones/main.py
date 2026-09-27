# Description:
# Imports the Mobile class from mobile.py and demonstrates
# creating multiple Mobile objects and calling their methods.

# Import the Mobile class from the other Python file
from mobile import Mobile

def main():
    # Create 4 Mobile objects with different attributes
    mobile1 = Mobile("Samsung", "Galaxy S24", "Android 15", "Blue")
    mobile2 = Mobile("iPhone", "15 Pro", "iOS 18.4.1", "Red")
    mobile3 = Mobile("Samsung", "Galaxy S23", "Android 14", "Gray")
    mobile4 = Mobile("iPhone", "15", "iOS 18.2.1", "Pink")

    # Display the phone details (attributes)
    phones = [mobile1, mobile2, mobile3, mobile4]
    for phone in phones:
        print(f"Make: {phone.make}")
        print(f"Model: {phone.model}")
        print(f"Operating System: {phone.os}")
        print(f"Color: {phone.color}\n")

    # Call some of the phone actions (methods)
    print("=== Phone Actions ===\n")
    mobile1.receive_call()
    mobile2.make_call()
    mobile3.stream_video()
    mobile4.play_game()


# Run the program
if __name__ == "__main__":
    main()

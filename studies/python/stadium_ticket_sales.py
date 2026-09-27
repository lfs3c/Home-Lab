# Description:
# Calculates the total ticket sales revenue for three seating classes:
# Class A ($20), Class B ($15), and Class C ($10), and displays the total.

# Variables for seat categories and prices
classA = ('Premium', 20)
classB = ('Standard', 15)
classC = ('Economy', 10)

def ticket_value(class_name, class_price, qty):
    """Calculates and displays subtotal for each seat class."""
    total = class_price * qty
    print(f'{class_name} Seats: {qty} - Total: ${total:,.2f}')
    return total

def main():
    print('\nWelcome to BCC Stadium Ticket Sales!')
    print(f'{classA[0]} Seats: ${classA[1]} each')
    print(f'{classB[0]} Seats: ${classB[1]} each')
    print(f'{classC[0]} Seats: ${classC[1]} each\n')

    try:
        qtyA = int(input('Enter the number of Premium tickets: '))
        qtyB = int(input('Enter the number of Standard tickets: '))
        qtyC = int(input('Enter the number of Economy tickets: '))

        totalA = ticket_value(classA[0], classA[1], qtyA)
        totalB = ticket_value(classB[0], classB[1], qtyB)
        totalC = ticket_value(classC[0], classC[1], qtyC)

        grand_total = totalA + totalB + totalC
        print(f'\nTotal ticket sales revenue: ${grand_total:,.2f}')

    except ValueError:
        print('Invalid input. Please enter whole numbers only.')

if __name__ == "__main__":
    main()

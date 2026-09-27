#This Python program simulates a traffic court judge deciding speeding cases in New Jersey. The script takes the posted speed limit and the driver’s recorded speed as input, 
#calculates how many miles over the limit the driver was traveling, and determines whether the driver should receive a fine and penalty points. 
#If the driver is not speeding, the program confirms no fines or points.

sspeedLimit = int(input('Please inform posted speed limit: \n'))  # Get from user the speed limit
actualSpeed = int(input('Please inform the actual speed the car was: \n'))  # Get from user the actual speed of the car

# Calculate how many miles over the speed limit
speedOverLimit = actualSpeed - speedLimit  

# Use if / elif / else to compare the excess speed to the points and fines assessed
# Speed Over Limit    Fine        Points
# 1-9 mph             $85         2
# 10-14 mph           $95         2
# 15-19 mph           $105        4
# 20-24 mph           $200        4
# 25-29 mph           $220        4
# 30-34 mph           $240        5
# 35-39 mph           $269        5

if speedOverLimit >= 35 and speedOverLimit <= 39:  # Check if the speed over limit fits in this range
    points = 5
    fine = 'USD 269.00'
elif speedOverLimit >= 30:
    points = 5
    fine = 'USD 240.00'
elif speedOverLimit >= 25:
    points = 4
    fine = 'USD 220.00'
elif speedOverLimit >= 20:
    points = 4
    fine = 'USD 200.00'
elif speedOverLimit >= 15:
    points = 4
    fine = 'USD 105.00'
elif speedOverLimit >= 10:
    points = 2
    fine = 'USD 95.00'
elif speedOverLimit >= 1:
    points = 2
    fine = 'USD 85.00'
# The else statement will catch all. In case the person wasn't actually speeding.
else:
    points = 0
    fine = 'USD 0.00'

# Now to print it. Use an if / else.
if speedOverLimit >= 1:  # If the car was speeding print:
    print(
        "This person was driving at", actualSpeed, "in a", speedLimit, "mph area.\n",
        "That means", speedOverLimit, "miles over the speed limit.\n",
        "This person will receive a fine of:", fine, "\n",
        "and", points, "points on their driving record."
    )
else:  # If the car was not speeding print:
    print("This driver was not speeding.")

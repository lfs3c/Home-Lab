#This Python program calculates how much the ocean level will rise over the next 25 years, 
#assuming a constant increase of 1.6 millimeters per year. It uses a while loop to display the 
#cumulative rise for each year, formatting the results to two decimal places for clarity.

totalYears = 25 #The total of year this program will run
oceanLevel = 1.6 #Rate of Ocean's Level rise per year
year = 1 #The first year
while year <= totalYears: #While variable year is <= 25
newLevel = year * oceanLevel #Variable newLevel
print(f'In the Year: {year}, the Ocean Level is: {newLevel:.2f}') #Using f-
strings to set the newLevel with 2. decimals
year += 1 #Variable year add 1

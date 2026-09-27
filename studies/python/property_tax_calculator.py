# Description:
# Calculates the assessment value of a property (60% of actual value)
# and determines the property tax at a rate of $0.72 per $100 assessed.

# Get the property value from the user
try:
    property_value = float(input('Please inform the actual value of the property: $'))

    # Calculate the assessment value (60% of the property value)
    assessment_value = property_value * 0.6

    # Calculate the property tax ($0.72 per $100 of assessment value)
    property_tax = (assessment_value / 100) * 0.72

    # Display results
    print(f'\nThe property value is: ${property_value:,.2f}')
    print(f'Assessment value (60%): ${assessment_value:,.2f}')
    print(f'Property tax: ${property_tax:,.2f}')

except ValueError:
    print("Invalid input. Please enter a numeric value.")

# Description:
# Calculates and displays the state (5%) and county (2.5%) sales taxes
# for a given total monthly sales amount, as well as the combined total tax.

def main():
    STATE_TAX = 0.05
    COUNTY_TAX = 0.025

    try:
        total_sales = float(input('Enter total monthly sales amount: $'))

        # Calculate taxes
        state_sales_tax = total_sales * STATE_TAX
        county_sales_tax = total_sales * COUNTY_TAX
        total_tax = state_sales_tax + county_sales_tax

        # Display results
        print(f'\nTotal monthly sales: ${total_sales:,.2f}')
        print(f'State sales tax (5%): ${state_sales_tax:,.2f}')
        print(f'County sales tax (2.5%): ${county_sales_tax:,.2f}')
        print(f'Total sales tax: ${total_tax:,.2f}')

    except ValueError:
        print('Invalid input. Please enter a numeric value.')

if __name__ == "__main__":
    main()

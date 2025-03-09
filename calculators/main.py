# Import the financial_calculator module in the calculators package using an absolute import
from calculators.financial_calculator import FinancialCalculator

financial_calculator = FinancialCalculator()
monthly_interest = financial_calculator.monthly_interest(0.06)

# Print the monthly interest
print(monthly_interest)

def calculate_loan_amount(monthly_payment, monthly_interest_rate, nbr_payments):
    """
    Calculate the loan amount based on the monthly payment, monthly interest rate, and total number of payments.
    """	
    # Raise an error if the number of total payment is less than zero
    if nbr_payments <= 0:
        raise ValueError("The number of payments must be greater than zero.")

    loan_amount = (monthly_payment * ((1 + monthly_interest_rate) ** nbr_payments - 1)) / \
                  (monthly_interest_rate * (1 + monthly_interest_rate) ** nbr_payments)
    
    # Return the loan amount
    return loan_amount
# data collection inputs needed 
# principal // apr // years
# calculate monthly payment & show the user 


def main():
    print("Loan monthly payment calculator")
    print("")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the anual interest rate: "))
    years = int(input("Input amount of years: "))
    
    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    
    print ("The monthly payment for this loan is: $ %.2f"  %  monthly_payment)
    
main()
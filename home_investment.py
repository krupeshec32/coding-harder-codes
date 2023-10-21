home_value = input("Please enter your home value: ")
down_payment = input("Please enter your down payment: ")
loan_amount = int(home_value) - int(down_payment)
annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
loan_term_years = int(input("Enter the loan term in years: "))

# Calculate the monthly interest rate and number of monthly payments
monthly_interest_rate = (annual_interest_rate / 100) / 12
num_payments = loan_term_years * 12

# Calculate the monthly mortgage payment
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

# Print the monthly mortgage payment
print(f"Your approximate monthly mortgage payment is: ${monthly_payment:.2f}")

monthly_rent =input("Please enter monthly rent: ")
monthly_hoa =input("Please enter HOA mouthly: ")
property_tax_percentage =input("Please enter property_tax_percentage: ")



print("Calculation for 1 year")
print('******************')
yearly_morgage_paid = int(monthly_payment)*12
yearly_rent = int(monthly_rent)*12
yearly_hoa = int(monthly_hoa)*12
property_tax_yearly= (int(home_value)*float(property_tax_percentage))/100
yearly_profite_or_loss = int(yearly_rent) - (int(yearly_morgage_paid)+int(yearly_hoa)+float(property_tax_yearly))

print(f"Your approximate yearly mortgage payment is: ${yearly_morgage_paid:.2f}")
print(f"Your approximate yearly rent: ${yearly_rent:.2f}")
print(f"Your approximate yearly tax: ${property_tax_yearly:.2f}")
print(f"Your approximate yearly profite/loss: ${yearly_profite_or_loss:.2f}")


print("Calculation for 5 year")
print('******************')

five_yearly_morgage_paid = (yearly_morgage_paid*5)
five_yearly_rent = (yearly_rent*5)
five_property_tax_yearly = (property_tax_yearly*5)
five_yearly_profite_or_loss = (yearly_profite_or_loss*5)
print(f"Your approximate 5 year mortgage payment is: ${five_yearly_morgage_paid:.2f}")
print(f"Your approximate 5 year rent: ${five_yearly_rent:.2f}")
print(f"Your approximate 5 year tax: ${five_property_tax_yearly:.2f}")
print(f"Your approximate 5 year profite/loss: ${five_yearly_profite_or_loss:.2f}")

print('After 5 year Bank Remaining Balance and what if you sell home')

total_5_year_principal = (int(five_yearly_morgage_paid)*25)//100
total_5_year_interest_paid = (int(five_yearly_morgage_paid)*75)//100
remaining_bank_loan = int(loan_amount)-int(total_5_year_principal)
selling_price= float(input("Enter the selling price: "))
print(f"remaining balance to pay to bank: ${remaining_bank_loan:.2f}")
temp = int(selling_price)-int(down_payment)
total = temp+abs(five_yearly_profite_or_loss)
print(f"After selling: ${total:.2f}")



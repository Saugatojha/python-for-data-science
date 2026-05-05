# 🏦 NEPSE Loan Eligibility Checker
# You're building a simple bank loan eligibility checker for NEPSE investors. 
# A user enters their details and your program tells them if they qualify.
# Your program should:

# Take the user's name as input
# Take their monthly income as input (can have decimals
# Take their existing loan amount as input (can have decimals)
# Take their credit score as input (whole number)

user_name = input("Enter your name: ")
monthly_income=float(input("Enter your monthly income: "))
current_loan=float(input("Enter your exisiting loan: "))
credit_score=int(input("enter your credit score: "))

# Then check these conditions:
# if income is above 50000 AND credit score above 700 AND no existing loan:
#     → "Eligible for full loan"
# elif income is above 30000 AND credit score above 500:
#     → "Eligible for partial loan"
# else:
#     → "Not eligible"
# Print the result with the person's name in the message using f-string

if monthly_income > 50000 and current_loan == 0 and credit_score > 700:
    print(f"Hello {user_name} Sir/Mam, you are eligble to take full loan")
elif monthly_income > 30000 and credit_score >= 500:
    print(f"Hello {user_name} Sir/Mam, you are eligible for partial loan")
else:
    print(f"Hello {user_name} Sir/Mam, you are not eligible for loan")
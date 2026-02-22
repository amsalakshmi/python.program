print("🏦 EMI Calculator")

principal = float(input("Enter loan amount (Principal): ₹"))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (years): "))

# Convert annual rate to monthly rate
monthly_rate = annual_rate / (12 * 100)

# Total number of months
months = years * 12

# EMI formula
emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print("\n📊 Loan Details")
print(f"Loan Amount: ₹{principal}")
print(f"Interest Rate: {annual_rate}%")
print(f"Tenure: {years} years")

print(f"\n💰 Monthly EMI: ₹{round(emi, 2)}")
print(f"Total Payment: ₹{round(emi * months, 2)}")
print(f"Total Interest: ₹{round((emi * months) - principal, 2)}")
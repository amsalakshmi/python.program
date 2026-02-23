from datetime import date

print("📅 Age Calculator")

year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

birth_date = date(year, month, day)
today = date.today()

# Calculate difference
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Adjust if negative
if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print("\n🎂 Your Age:")
print(f"{years} Years, {months} Months, {days} Days")

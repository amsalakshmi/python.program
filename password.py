import re

def check_password_strength(password):
    strength = 0
    
    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Contains lowercase
    if re.search("[a-z]", password):
        strength += 1
    
    # Contains uppercase
    if re.search("[A-Z]", password):
        strength += 1
    
    # Contains digit
    if re.search("[0-9]", password):
        strength += 1
    
    # Contains special character
    if re.search("[@#$%^&+=!]", password):
        strength += 1
    
    # Strength result
    if strength <= 2:
        return "Weak Password ❌"
    elif strength == 3 or strength == 4:
        return "Medium Password ⚠️"
    else:
        return "Strong Password ✅"

# User input
pwd = input("Enter your password: ")
result = check_password_strength(pwd)
print("Password Strength:", result)

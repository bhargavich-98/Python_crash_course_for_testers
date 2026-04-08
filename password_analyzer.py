# Project: Password Analyzer

# Check:

# length
# uppercase
# digits
# special characters
# Return strength score (Weak/Medium/Strong)

password = input("Enter password to analyze:")
def analyze_password(password):
    score = 0
    if len(password) > 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        score += 1
    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    else:
        return "Strong"
strength = analyze_password(password)
print(f"Password strength: {strength}")

# Build: Login Validator Script

# Input username/password
# Check:
# length > 8
# contains number
# Print pass/fail
# Allow 3 attempts
# Lock after failures
# Show remaining attempts
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if len(password) > 8 and any(char.isdigit() for char in password):
        print("Pass")
        break
    else:
        attempts -= 1
        print(f"Fail. Remaining attempts: {attempts}")
        if attempts == 0:
            print("Account locked due to too many failed attempts.")


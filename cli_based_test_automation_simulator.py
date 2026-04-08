# Project - CLI-Based Test Automation Simulator
# Features:
# User login system
# Menu:
# Run tests
# View report
# Use:
# variables
# loops
# functions
# string processing
# f-strings
import time
users = {"admin": "password123"}    
test_results = []
def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username not in users:
            print("Username not found. Try again.")
        elif users[username] == password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. Remaining attempts: {attempts}")
    print("Too many failed attempts. Exiting.")
    return False

        
def run_tests():
    print("Running tests...")
    time.sleep(2)
    test_cases = ["Login Test", "Signup Test", "Checkout Test"]
    for test in test_cases:
        time.sleep(1)
        result = "pass" if len(test) % 2 ==0 else "fail"
        test_results.append((test, result))
        print(f"{test}: {result}")

def view_report():
    print("Test Report:")
    print("------------")
    if not test_results:
        print("No tests run yet.")
        return
    for test, result in test_results:
        print(f"{test}: {result}")
        print(f"Report generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}")
if login():
    while True:
        print("\nMenu:")
        print("1. Run tests")
        print("2. View report")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            run_tests()
        elif choice == '2':
            view_report()
        elif choice == '3':
            print("Exiting the simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
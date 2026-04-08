#Build a script that generates realistic test data (names, emails, phone numbers) and prints a formatted test report to the console.
import random
import string
def generate_random_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Miller"]
    return random.choice(first_names) + " " + random.choice(last_names)
def generate_random_email(name):
    domains = ["example.com", "test.com", "sample.com"]
    username = name.lower().replace(" ", ".")
    return username + "@" + random.choice(domains)
def generate_random_phone_number():
    return "(".join(random.choices(string.digits, k=3)) + ")" + "".join(random.choices(string.digits, k=3)) + "-" + "".join(random.choices(string.digits, k=4)) 
def generate_test_data(num_entries):
    test_data = []
    for _ in range(num_entries):
        name = generate_random_name()
        email = generate_random_email(name)
        phone_number = generate_random_phone_number()
        test_data.append({"name": name, "email": email, "phone_number": phone_number})
    return test_data
def print_test_report(test_data):
    print("Test Report:")
    print("------------")
    for entry in test_data:
        print(f"Name: {entry['name']}, Email: {entry['email']}, Phone Number: {entry['phone_number']}")
# Generate and print test data
test_data = generate_test_data(5)
print_test_report(test_data)
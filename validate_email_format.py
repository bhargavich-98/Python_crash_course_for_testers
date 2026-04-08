import re

regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def validate_email_format(email):
    if re.match(regex, email):
        return True
    else:
        return False
# Test cases
print(validate_email_format("test@example.com"))  # Should return True
print(validate_email_format("invalid.email"))     # Should return False

def even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# difference between list and tuple
# List is mutable, meaning you can change its contents after it has been created. You can add, remove, or modify elements in a list. Lists are defined using square brackets [].
# Tuple is immutable, meaning once it is created, you cannot change its contents. You cannot add, remove, or modify elements in a tuple. Tuples are defined using parentheses ().   

# Project: Test Report Generator
# formatting
# expressions inside strings
# Print multiple test cases in loop
# Add timestamps

from datetime import datetime
test_cases = [
    {"name": "Test Case 1", "status": "Pass"},
    {"name": "Test Case 2", "status": "Fail"},
    {"name": "Test Case 3", "status": "Pass"},
]   
def print_test_report(test_cases):
    print("Test Report:")
    print("------------")
    for case in test_cases:
        print(f"{case['name']}: {case['status']}")
    print(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print_test_report(test_cases)


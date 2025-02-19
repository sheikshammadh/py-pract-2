# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

# Test the function
number = 42
result = check_odd_even(number)
print(result)  # Output: 42 is even

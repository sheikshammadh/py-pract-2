# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
number = 29
result = is_prime(number)
print(f"{number} is prime: {result}")  # Output: 29 is prime: True

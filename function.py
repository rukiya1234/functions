# Function Exercises

# 1. Square of a number
def square(n):
    return n * n

# 2. Palindrome check
def is_palindrome(s):
    return s == s[::-1]

# 3. Decorator to log execution time
import time
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.6f}s")
        return result
    return wrapper

# 4. Generator for infinite primes
def infinite_primes():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            yield num
        num += 1

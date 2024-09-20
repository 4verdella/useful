#usul_1
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
print(factorial(5))  # Output: 120



#usul_2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120



#usul_3
import math

# Example usage:
print(math.factorial(5))
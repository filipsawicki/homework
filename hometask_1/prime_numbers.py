"""
Prime numbers
"""
import math
def is_prime(num):
    """Return True if num is a prime number. False otherwise. """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(num))
    for i in range(2, 1 + max_divisor):
        if num % i == 0:
            return False
    return True


print(is_prime(100))

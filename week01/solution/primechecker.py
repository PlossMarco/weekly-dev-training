"""
Thies module contains a function to check if a number is prime or not.
"""


def is_prime(n):
    """This function checks if a number is prime or not."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(1))  # False
    print(is_prime(2))  # True
    print(is_prime(3))  # True
    print(is_prime(4))  # False
    print(is_prime(5))  # True
    print(is_prime(10)) # False
    print(is_prime(11)) # True

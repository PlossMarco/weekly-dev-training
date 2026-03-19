"""
This module gives n- first prime numbers.
"""


def is_prime(n):
    """This function checks if a number is prime or not."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """This function gives n- first prime numbers."""
    primes =[]
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

if __name__ == "__main__":
    for prim in get_primes(55):
        print(prim)
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be greater than 0.")
    list = []
    # It would be incredibly inefficient to check every single number for being prime. E.g., check if 1 is prime, then 2, then 3, then 4, then 5, ... until we reach a count of 10 primes.
    i = 2
    while len(list) < number_of_primes:
        if is_prime(i):
            list.append(i)
        i += 1
    return list

def is_prime(num: int) -> bool:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

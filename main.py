# Problem 47:
#     Distinct Primes Factors
#
# Description:
#     The first two consecutive numbers to have two distinct prime factors are:
#         14 = 2 × 7
#         15 = 3 × 5
#
#     The first three consecutive numbers to have three distinct prime factors are:
#         644 = 2² × 7 × 23
#         645 = 3 × 5 × 43
#         646 = 2 × 17 × 19.
#
#     Find the first four consecutive integers to have four distinct prime factors each.
#     What is the first of these numbers?

from math import floor, sqrt


def main(n):
    """
    For a given `n`,
      returns the least of the first `n` consecutive natural numbers
      to each have `n` distinct prime factors.

    Args:
        n (int): Natural number

    Returns:
        (int): Least of the first `n` consecutive natural numbers to each have `n` distinct prime factors.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    prime_list = []
    prime_set = set()

    # Loop upwards through natural numbers
    # (Consider 0 and 1 as having 0 prime factors)
    x = 2
    seen = 0
    while True:
        # Check whether x is prime by counting its prime factors
        # Break down x by continually dividing until it is 1 or prime
        y = x
        x_prime_factors = set()
        i = 0
        y_mid = floor(sqrt(y)) + 1
        while y > 1 and y not in prime_set and i < len(prime_list) and prime_list[i] < y_mid:
            p = prime_list[i]
            if y % p == 0:
                x_prime_factors.add(p)
                while y % p == 0:
                    y //= p
            i += 1
        if y in prime_set:
            x_prime_factors.add(y)

        if len(x_prime_factors) == n:
            seen += 1  # Increment the consecutive count
            if seen == n:
                return x - n + 1
        else:
            seen = 0  # Reset the consecutive count
            if len(x_prime_factors) == 0:
                # Wasn't divisible by any of the primes found so far, so must be a prime itself
                prime_list.append(x)
                prime_set.add(x)
        x += 1


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    first_val = main(num)
    print('First {0} consecutive integers to have {0} distinct prime factors each:'.format(num))
    for step in range(num):
        print('  {}'.format(first_val+step))

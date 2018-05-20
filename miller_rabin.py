import random


# 3 - Miller-Rabin Test
def is_prime(n, iterations=40):
    """Rabin-Miller Primality Test.
    Utilize the Rabin-Miller test to determinate if a number is
    a prime number or not.

    Args:
        n: number to be tested.
        iterations: how many tries with random numbers must be
        applied. [default: 40]
    Return:
        True if the number pass the Rabin-Miller test, False otherwise.
    """
    # if the number is 1, 2 or even, the result is directly given
    if n in [1, 2]:
        return True
    if n % 2 == 0:
        return False

    # recalculate m until it is not even anymore, and keeps track
    # of how many iteration were needed.
    s, m = 0, n - 1
    while m % 2 == 0:
        m = m // 2
        s += 1

    # for the chosen number of iterations, it generates a random number 'a'
    # between 2 and n -1 and it calculates 2^m mod n
    for _ in range(iterations):
        a = random.randrange(2, n - 1)
        x = pow(a, m, n)
        # The rules of the Miller-Rabin test are applied. If x is 1 or n - 1
        # skips to the next value in range. Otherwise, calculate x^2 mod n and
        # check that it must not be equal to n - 1
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        return False
    return True


# 4 - Prime Number Generator
def prime_generator(k):
    """Keeps generating random integers of length k until
    it founds a prime number.

    Args:
        k: lenght of the requested number.
    Return:
        A prime number of length k.
    """
    while True:
        n = random.randint(10**(k-1), 10**k-1)
        if is_prime(n):
            return n

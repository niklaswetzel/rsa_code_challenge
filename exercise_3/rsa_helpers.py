import numpy as np
import math


def extended_euclidean(a, b):
    """
    Solves the equation gcd(a,b) = s*a + t*b
    :param a: int
    :param b: int
    :return: tuple
         gcd(a,b), s, t
    """
    ...


def create_private_key(prime_0, prime_1, public_key=2**16 + 1):
    """
    Returns the private key of the RSA method.
    For N = prime_0*prime_1, the private key solves the equation

    ``m = ((m**public_key)**private_key) % N``

    for any 0 <= m < N .

    :param prime_0: int
        prime number
    :param prime_1: int
        prime number
    :param public_key: int
        Has to be co-prime to lcm(prime_0-1, prime_1-1) (least common multiple)
        Defaults to 2**16 + 1
    :return: int
    """
    ...

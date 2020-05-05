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
    # init
    r_nm1 = a
    s_nm1 = 1
    t_nm1 = 0

    r_n = b
    s_n = 0
    t_n = 1

    while True:
        q_np1 = r_nm1 // r_n
        # update r
        r_nm1, r_n = r_n, r_nm1 % r_n

        # update s, t
        s_nm1, s_n = s_n, s_nm1 - q_np1*s_n
        t_nm1, t_n = t_n, t_nm1 - q_np1*t_n
        if r_n == 0:
            # print(f'{r_nm1} = {s_nm1}*{a} + {t_nm1}*{b}')
            assert r_nm1 == s_nm1*a + t_nm1*b
            return r_nm1, s_nm1 , t_nm1


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
    carmichael = _lcm(prime_0-1, prime_1-1)
    a = public_key
    b = carmichael

    # Bezu identity: r = s*e + t*carmichael
    r, s, t = extended_euclidean(a, b)
    if r != 1:
        print(f"public key {public_key} and carmichaels number {carmichael} are not co-prime!")
        raise ValueError

    return s if s > 0 else s % carmichael


def _gcd(a, b):
    # return np.gcd(a, b)  # installation needed
    return math.gcd(a,b)


def _lcm(a, b):
    # return np.lcm(a, b) #  installation needed
    return abs(a*b//_gcd(a,b))
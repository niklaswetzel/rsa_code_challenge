from exercise_3.rsa_helpers import create_private_key


class RSA(object):
    """
    Implements the RSA algorithm.
    """

    def __init__(self, prime_0, prime_1, public_key=2**16+1):
        ...

    def encrypt(self, org_message_number):
        ...

    def decrypt(self, enc_message_number, key=None):
        ...


from exercise_3.rsa_helpers import create_private_key


class RSA(object):
    """
    Implements the RSA algorithm.
    """

    def __init__(self, prime_0, prime_1, public_key=2**16+1):

        self.alphabet_length = prime_0*prime_1
        self.public_key = public_key
        self.private_key = create_private_key(prime_0, prime_1, public_key)

    def encrypt(self, org_message_number):
        return self.decrypt(org_message_number, key=self.public_key)

    def decrypt(self, enc_message_number, key=None):
        if not key:
            key = self.private_key
        bin_str = bin(key)[2:]
        bin_str_rev = bin_str[::-1]

        r_iter = enc_message_number
        r_prod = 1

        for dig in bin_str_rev:
            if dig == '1':
                r_prod *= r_iter
            r_iter = (r_iter ** 2) % self.alphabet_length

        return r_prod % self.alphabet_length


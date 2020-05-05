from functools import partial

from exercise_1.convert_text import split_to_messages, join_to_plaintext
from exercise_2.bit_representation import to_int, to_message
from exercise_4.rsa import RSA


class Cipher(object):
    """
    Encrypts `plaintext` to `cipher_list` and decrypts `cipher_list` to `plaintext` with the RSA algorithm
    """

    def __init__(
            self,
            char_bit_len,
            prime_0,
            prime_1,
            public_key,
    ):
        ...

    def encrypt(self, plaintext):
        ...

    def decrypt(self, cipher_list):
        ...

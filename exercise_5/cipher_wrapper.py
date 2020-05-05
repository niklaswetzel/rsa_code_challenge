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
        self.char_bit_len = char_bit_len
        self.rsa = RSA(prime_0, prime_1, public_key)

    def encrypt(self, plaintext):
        message_list = split_to_messages(
            plaintext,
            alphabet_len=self.rsa.alphabet_length,
            char_bit_len=self.char_bit_len
        )
        to_int_part = partial(to_int, char_bit_len=self.char_bit_len)
        int_rep_iter = map(to_int_part, message_list)
        cipher_list = list(map(self.rsa.encrypt, int_rep_iter))

        return cipher_list

    def decrypt(self, cipher_list):

        int_rep_iter = map(self.rsa.decrypt, cipher_list)
        to_message_part = partial(to_message, char_bit_len=self.char_bit_len)
        message_iter = map(to_message_part, int_rep_iter)
        plaintext = join_to_plaintext(message_iter)

        return plaintext

import unittest

from exercise_5.cipher_wrapper import Cipher


class TestCipherWrapper(unittest.TestCase):

    def test_00(self):
        self.c = Cipher(
            char_bit_len=7,
            prime_0=61,
            prime_1=53,
            public_key=17,
        )

        plaintext = "Hello World"
        ciphertext = self.c.encrypt(plaintext)
        dec_text = self.c.decrypt(ciphertext)
        my_res = dec_text, ciphertext
        cor_res = "Hello World", [3000, 1313, 745, 745, 2185, 1992, 604, 2185, 2412, 745, 1773]

        print(f'Out[0]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_01(self):
        self.c = Cipher(
            char_bit_len=7,
            prime_0=61,
            prime_1=53,
            public_key=17,
        )

        plaintext = "I have the feeling someone is listening. We are not alone here!"
        ciphertext = self.c.encrypt(plaintext)
        dec_text = self.c.decrypt(ciphertext)
        my_res = dec_text, ciphertext
        cor_res = "I have the feeling someone is listening. We are not alone here!",[
            1486,
            1992,
            2170,
            1632,
            2578,
            1313,
            1992,
            884,
            2170,
            1313,
            1992,
            1369,
            1313,
            1313,
            745,
            3179,
            2235,
            2923,
            1992,
            1230,
            2185,
            2271,
            1313,
            2185,
            2235,
            1313,
            1992,
            3179,
            1230,
            1992,
            745,
            3179,
            1230,
            884,
            1313,
            2235,
            3179,
            2235,
            2923,
            2825,
            1992,
            604,
            1313,
            1992,
            1632,
            2412,
            1313,
            1992,
            2235,
            2185,
            884,
            1992,
            1632,
            745,
            2185,
            2235,
            1313,
            1992,
            2170,
            1313,
            2412,
            1313,
            1853
        ]
        print(f'Out[1]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_02(self):
        self.c = Cipher(
            char_bit_len=7,
            prime_0=113,
            prime_1=59,
            public_key=19,
        )

        plaintext = "No, I think its just impossible to crack the code!"
        ciphertext = self.c.encrypt(plaintext)
        dec_text = self.c.decrypt(ciphertext)
        my_res = dec_text, ciphertext
        cor_res = "No, I think its just impossible to crack the code!", [
            5037,
            6360,
            208,
            6116,
            1879,
            6116,
            871,
            3431,
            1693,
            5457,
            4029,
            6116,
            1693,
            871,
            1776,
            6116,
            6132,
            4188,
            1776,
            871,
            6116,
            1693,
            5982,
            4745,
            6360,
            1776,
            1776,
            1693,
            128,
            2917,
            231,
            6116,
            871,
            6360,
            6116,
            509,
            453,
            2550,
            509,
            4029,
            6116,
            871,
            3431,
            231,
            6116,
            509,
            6360,
            5573,
            231,
            5412
        ]
        print(f'Out[2]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_03(self):
        self.c = Cipher(
            char_bit_len=7,
            prime_0=447816969936417125298328813691,
            prime_1=662071711764943530683672047777,
            public_key=2**16 + 1,
        )

        plaintext = "I increased the security level, just to be sure."
        ciphertext = self.c.encrypt(plaintext)
        dec_text = self.c.decrypt(ciphertext)
        my_res = dec_text, ciphertext
        cor_res = "I increased the security level, just to be sure.", [
            181219457771084548292619429468118353121812403968963096957357,
            106322765049049829500697686490142929405441029793391526055840
        ]

        print(f'Out[3]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_04(self):
        self.c = Cipher(
            char_bit_len=7,
            prime_0=11,
            prime_1=17,
            public_key=3,
        )

        plaintext = "Completely unnecessary!"
        ciphertext = self.c.encrypt(plaintext)
        dec_text = self.c.decrypt(ciphertext)
        my_res = dec_text, ciphertext
        cor_res = "Completely unnecessary!", [
            67,
            100,
            54,
            184,
            80,
            118,
            7,
            118,
            80,
            110,
            43,
            145,
            121,
            121,
            118,
            143,
            118,
            4,
            4,
            113,
            130,
            110,
            33
        ]

        print(f'Out[4]: {my_res}')
        self.assertEqual(my_res, cor_res)


if __name__ == '__main__':
    unittest.main()

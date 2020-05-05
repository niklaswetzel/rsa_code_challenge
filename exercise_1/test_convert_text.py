import unittest

from exercise_1.convert_text import split_to_messages, join_to_plaintext


class TestConvertText(unittest.TestCase):

    # split_to_messages tests
    def test_00(self):
        my_res = split_to_messages('a', 2 ** 7)
        cor_res = list('a')
        print(f'Out[0]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_01(self):
        my_res = split_to_messages('abcxyz!', 2 ** 7)
        cor_res = list('abcxyz!')
        print(f'Out[1]: {my_res}')
        self.assertEqual(my_res,cor_res)

    def test_02(self):
        my_res = split_to_messages('abcxyz!', 2 ** 8 - 1)
        cor_res = list('abcxyz!')
        print(f'Out[2]: {my_res}')
        self.assertEqual(my_res,cor_res)

    def test_03(self):
        my_res = split_to_messages('abcxyz!', 2 ** 6, char_bit_len=6)
        cor_res = list('abcxyz!')
        print(f'Out[3]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_04(self):
        my_res = split_to_messages('abcd', 2 ** 14)
        cor_res = ['ab', 'cd']
        print(f'Out[4]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_05(self):
        my_res = split_to_messages('abc ', 2 ** 10, char_bit_len=5)
        cor_res = ['ab', 'c ']
        print(f'Out[5]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_06(self):
        my_res = split_to_messages('Hello World!', 2 ** (10 * 7))
        cor_res = ['Hello Worl', 'd!        ']
        print(f'Out[6]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_07(self):
        my_res = split_to_messages('Hello World!', 2 ** (10 * 7) - 1)
        cor_res = ['Hello Wor', 'ld!      ']
        print(f'Out[7]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_08(self):
        my_res = split_to_messages(
            'A very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, long text!',
            2 ** (10 * 7) - 1
        )
        cor_res = [
            'A very, v',
            'ery, very',
            ', very, v',
            'ery, very',
            ', very, v',
            'ery, very',
            ', very, v',
            'ery, very',
            ', very, v',
            'ery, very',
            ', long te',
            'xt!      '
        ]

        print(f'Out[8]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_09(self):
        long_text = 'A very, very, very, very, very, very, very, ' \
                    'very, very, very, very, very, very, very, very, very, very, long text!'
        text_len = len(long_text)
        my_res = split_to_messages(long_text, 2 ** (text_len * 7))
        cor_res = [long_text,]
        print(f'Out[9]: {my_res}')
        self.assertEqual(my_res, cor_res)

    # join_to_plaintext tests
    def test_10(self):
        message_list = ['Hello Worl', 'd!        ']
        my_res = join_to_plaintext(message_list)
        cor_res = 'Hello World!'
        print(f'Out[10]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_11(self):
        message_list = ['Divide and', ' Conquer!!']
        my_res = join_to_plaintext(message_list)
        cor_res = 'Divide and Conquer!!'
        print(f'Out[11]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_12(self):
        message_list = ['sinlge_is_better',]
        my_res = join_to_plaintext(message_list)
        cor_res = 'sinlge_is_better'
        print(f'Out[12]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_13(self):
        message_list = ['  ', '#$', '%^', '&*', '()', '%^', '&*', '()', '_ ', '  ']
        my_res = join_to_plaintext(message_list)
        cor_res = '  #$%^&*()%^&*()_'
        print(f'Out[13]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_14(self):
        message_list = list('A very looooooooooooooooooooooooooooooooooong list! ')
        my_res = join_to_plaintext(message_list)
        cor_res = 'A very looooooooooooooooooooooooooooooooooong list!'
        print(f'Out[14]: {my_res}')
        self.assertEqual(my_res, cor_res)


if __name__ == '__main__':
    unittest.main()

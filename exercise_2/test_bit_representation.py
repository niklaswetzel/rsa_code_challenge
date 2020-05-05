import unittest

from exercise_2.bit_representation import to_int, to_message


class TestBitRepresentation(unittest.TestCase):

    def test_00(self):
        my_res = to_int('a')
        cor_res = 97
        print(f'Out[0]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_01(self):
        my_res = to_int('az')
        cor_res = 0b11000011111010
        print(f'Out[1]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_02(self):
        my_res = to_int('az',8)
        cor_res = 0b0110000101111010
        print(f'Out[2]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_03(self):
        my_res = to_int('abcdefghi')
        cor_res = 7045194587020325993
        print(f'Out[3]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_04(self):
        my_res = to_int('abcd',10)
        cor_res = 0b0001100001000110001000011000110001100100
        print(f'Out[4]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_05(self):
        my_res = to_int('Hello World!')
        cor_res = 11000576099255459178557985
        print(f'Out[5]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_06(self):
        my_res = to_int('!@#$%^&*()_+')
        cor_res = 5062702302974816629190571
        print(f'Out[6]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_07(self):
        my_res = to_int('10000000000000000000000000000000000')
        cor_res = 21810822722884346714206414620391421284949117160053162374764945843122083888
        print(f'Out[7]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_08(self):
        my_res = to_int('  ', 14)
        cor_res = 0b0000000010000000000000100000
        print(f'Out[8]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_09(self):
        my_res = to_int('aa')
        cor_res = 0b11000011100001
        print(f'Out[9]: {my_res}')
        self.assertEqual(my_res, cor_res)

    # to_message tests
    def test_10(self):
        my_res = to_message(97)
        cor_res = 'a'
        print(f'Out[10]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_11(self):
        my_res = to_message(0b11000011111010)
        cor_res = 'az'
        print(f'Out[11]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_12(self):
        my_res = to_message(11000576099255459178557985)
        cor_res = 'Hello World!'
        print(f'Out[12]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_13(self):
        my_res = to_message(5062702302974816629190571)
        cor_res = '!@#$%^&*()_+'
        print(f'Out[13]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_14(self):
        my_res = to_message(24954,8)
        cor_res = 'az'
        print(f'Out[14]: {my_res}')
        self.assertEqual(my_res, cor_res)



if __name__ == '__main__':
    unittest.main()

import unittest

from exercise_3.rsa_helpers import extended_euclidean, create_private_key


class TestRsaHelpers(unittest.TestCase):

    # extended_euclidean tests
    def test_00(self):
        my_res = extended_euclidean(12312, 56)
        cor_res = (8, -1, 220)
        print(f'Out[00]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_01(self):
        my_res = extended_euclidean(456,232)
        cor_res = (8, -1, 2)
        print(f'Out[1]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_02(self):
        my_res = extended_euclidean(160487, 1987)
        cor_res = (1, -419, 33842)
        print(f'Out[2]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_03(self):
        my_res = extended_euclidean(2**16 + 1, 2*3*4*5*6*7)
        cor_res = (1, 593, -7711)
        print(f'Out[03]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_04(self):
        my_res = extended_euclidean(2*3*5*7*11*13*15, 2*3*5*7*11*13*17)
        cor_res = (30030, 8, -7)
        print(f'Out[4]: {my_res}')
        self.assertEqual(my_res, cor_res)

    # create_private_key tests
    def test_05(self):
        my_res = create_private_key(61, 53, 17)
        cor_res = 413
        print(f'Out[5]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_06(self):
        my_res = create_private_key(5, 11, 3)
        cor_res = 7
        print(f'Out[6]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_07(self):
        my_res = create_private_key(113, 59, 17)
        cor_res = 3057
        print(f'Out[7]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_08(self):
        my_res = create_private_key(
            447816969936417125298328813691,
            662071711764943530683672047777,
            2**16 + 1,
        )
        cor_res = 39774680645091492334610709018817613892653866020350490752513
        print(f'Out[8]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_09(self):
        my_res = create_private_key(
            6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,  # M_521
            531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127,  # M_607
            2**16 + 1,
        )
        cor_res = 605309440029444797632079365922351903778944636504290628815687804447518401725202045830587428993072200378798732205389608178468869002370652053408838463061590768976059755211666722868590174546762165023955171158423681809701058604934000382033836393559131564093520170601086332978178762009136501271874027235396379522707933355224417396404416034089473
        print(f'Out[9]: {my_res}')
        self.assertEqual(my_res, cor_res)


if __name__ == '__main__':
    unittest.main()

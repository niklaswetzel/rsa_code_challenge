import unittest

from exercise_4.rsa import RSA


class TestRSA(unittest.TestCase):

    # test attributes
    def test_00(self):
        self.rsa = RSA(61, 53, 17)
        my_res = self.rsa.alphabet_length, self.rsa.public_key, self.rsa.private_key
        cor_res = 61*53, 17, 413

        print(f'Out[0]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_01(self):
        self.rsa = RSA(5, 11, 3)
        my_res = self.rsa.alphabet_length, self.rsa.public_key, self.rsa.private_key
        cor_res = 5*11, 3, 7

        print(f'Out[1]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_02(self):
        self.rsa = RSA(113, 59, 17)
        my_res = self.rsa.alphabet_length, self.rsa.public_key, self.rsa.private_key
        cor_res = 113 * 59, 17, 3057

        print(f'Out[2]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_03(self):
        self.rsa = RSA(
            447816969936417125298328813691,
            662071711764943530683672047777,
            2**16 + 1,
        )
        my_res = self.rsa.alphabet_length, self.rsa.public_key, self.rsa.private_key
        cor_res = 447816969936417125298328813691*662071711764943530683672047777, 2**16 + 1, 39774680645091492334610709018817613892653866020350490752513

        print(f'Out[3]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_04(self):
        self.rsa = RSA(
            6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,  # M_521
            531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127,  # M_607
            2**16 + 1,
        )
        my_res = self.rsa.alphabet_length, self.rsa.public_key, self.rsa.private_key
        cor_res = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151*531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127,\
                  2**16 + 1,\
                  605309440029444797632079365922351903778944636504290628815687804447518401725202045830587428993072200378798732205389608178468869002370652053408838463061590768976059755211666722868590174546762165023955171158423681809701058604934000382033836393559131564093520170601086332978178762009136501271874027235396379522707933355224417396404416034089473

        print(f'Out[4]: {my_res}')
        self.assertEqual(my_res, cor_res)

    # test encrypt
    def test_05(self):
        self.rsa = RSA(61, 53, 17)

        my_res = self.rsa.encrypt(65)
        cor_res = 2790
        print(f'Out[5]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_06(self):
        self.rsa = RSA(5, 11, 3)
        self.assertEqual(self.rsa.alphabet_length, 5*11)
        self.assertEqual(self.rsa.public_key, 3)
        self.assertEqual(self.rsa.private_key, 7)

        my_res = self.rsa.encrypt(6)
        cor_res = 51
        print(f'Out[6]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_07(self):
        self.rsa = RSA(113, 59, 17)
        self.assertEqual(self.rsa.alphabet_length, 113*59)
        self.assertEqual(self.rsa.public_key, 17)
        self.assertEqual(self.rsa.private_key, 3057)
        my_res = self.rsa.encrypt(65)
        cor_res = 4698
        print(f'Out[7]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_08(self):
        self.rsa = RSA(
            447816969936417125298328813691,
            662071711764943530683672047777,
            2**16 + 1,
        )
        self.assertEqual(self.rsa.alphabet_length, 447816969936417125298328813691*662071711764943530683672047777)
        self.assertEqual(self.rsa.public_key, 2**16 + 1)
        self.assertEqual(self.rsa.private_key, 39774680645091492334610709018817613892653866020350490752513)

        my_res = self.rsa.encrypt(17021988)
        cor_res = 83255976628534078919435758300508116586045703387071504707082
        print(f'Out[8]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_09(self):
        self.rsa = RSA(
            6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,  # M_521
            531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127,  # M_607
            2**16 + 1,
        )

        my_res = self.rsa.encrypt(160487)
        cor_res = 2798726042245842547489988545039525086333744716331222623018390997534600757827401890007289448816597823910120916855280546522159522329872590185624975306113008697227355293751247676715667770597058214972358906603669350996411631591142042057474047061125764754322092438628729841442694021121336346685743578921137362618702191455448574841928993116305428
        print(f'Out[9]: {my_res}')
        self.assertEqual(my_res, cor_res)

    # tests decrypt 
    def test_10(self):
        self.rsa = RSA(61, 53, 17)
        my_res = self.rsa.decrypt(2790)
        cor_res = 65
        print(f'Out[10]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_11(self):
        self.rsa = RSA(5, 11, 3)
        my_res = self.rsa.decrypt(51)
        cor_res = 6
        print(f'Out[11]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_12(self):
        self.rsa = RSA(113, 59, 17)
        my_res = self.rsa.decrypt(4698)
        cor_res = 65
        print(f'Out[12]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_13(self):
        self.rsa = RSA(
            447816969936417125298328813691,
            662071711764943530683672047777,
            2**16 + 1,
        )

        my_res = self.rsa.decrypt(83255976628534078919435758300508116586045703387071504707082)
        cor_res = 17021988
        print(f'Out[13]: {my_res}')
        self.assertEqual(my_res, cor_res)

    def test_14(self):
        self.rsa = RSA(
            6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,
            # M_521
            531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127,
            # M_607
            2 ** 16 + 1,
        )

        my_res = self.rsa.decrypt(2798726042245842547489988545039525086333744716331222623018390997534600757827401890007289448816597823910120916855280546522159522329872590185624975306113008697227355293751247676715667770597058214972358906603669350996411631591142042057474047061125764754322092438628729841442694021121336346685743578921137362618702191455448574841928993116305428)
        cor_res = 160487

        print(f'Out[14]: {my_res}')
        self.assertEqual(my_res, cor_res)


if __name__ == '__main__':
    unittest.main()

import unittest

import numpy as np

from Hill_Cipher import Hill_Cipher
from Rail_Fence_Cipher import Rail_Fence_Cipher
from Vigenere_Cipher import Vigenere_Cipher


def cetak_hasil(result, expected):
    print("result  :", result)
    print("expected:", expected)


class TestHillCipher(unittest.TestCase):
    def setUp(self):
        self.hc = Hill_Cipher()
        self.key_array = np.array([
            [17, 17, 5],
            [21, 18, 21],
            [2, 2, 19]
        ])

    def testGenerateKeyArray(self):
        print("\n- Hill_Cipher.generateKeyArray")
        result = self.hc.generateKeyArray("RRFVSVCCT")
        expected = self.key_array.tolist()
        cetak_hasil(result.tolist(), expected)
        self.assertCountEqual(result.tolist(), expected)

    def testFindDeterminant(self):
        print("\n- Hill_Cipher.findDeterminant")
        result = self.hc.findDeterminant(self.key_array)
        cetak_hasil(result, -939)
        self.assertEqual(result, -939)

    def testFindAdjoint(self):
        print("\n- Hill_Cipher.findAdjoint")
        result = self.hc.findAdjoint(self.key_array)
        expected = [[14, 25,  7], [7, 1, 8], [6, 0, 1]]
        cetak_hasil(result.tolist(), expected)
        self.assertCountEqual(result.tolist(), expected)

    def testFindInvMod(self):
        print("\n- Hill_Cipher.findInvMod")
        result = self.hc.findInvMod(23, 26)
        cetak_hasil(result, 17)
        self.assertEqual(result, 17)

    def testEncrypt(self):
        print("\n- Hill_Cipher.encrypt")
        result = self.hc.encrypt("help me", "RRFVSVCCT")
        expected = "RFQVLN"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)

    def testDecrypt(self):
        print("\n- Hill_Cipher.decrypt")
        result = self.hc.decrypt("RFQVLN", "RRFVSVCCT")
        expected = "HELPME"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)


class TestRailFenceCipher(unittest.TestCase):
    def setUp(self):
        self.rfc = Rail_Fence_Cipher()

    def testGenerateOrdArray(self):
        print("\n- Rail_Fence_Chiper.generateOrdArray")
        result = self.rfc.generateOrdArray("help me")
        expected = [7, 4, 11, 15, 12, 4]
        cetak_hasil(result.tolist(), expected)
        self.assertCountEqual(result.tolist(), expected)

    def testFillingField(self):
        print("\n- Rail_Fence_Chiper.fillingField")
        result = self.rfc.fillingField("help me", 2)
        expected = [[None, 'e', None, 'p', None, 'm', None],
                    ['h', None, 'l', None, ' ', None, 'e']]
        cetak_hasil(result.tolist(), expected)
        self.assertCountEqual(result.tolist(), expected)

    def testEncrypt(self):
        print("\n- Rail_Fence_Chiper.encrypt")
        result = self.rfc.encrypt("help me", 2)
        expected = "EPEHLM"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)

    def testDecrypt(self):
        print("\n- Rail_Fence_Chiper.decrypt")
        result = self.rfc.decrypt("EPEHLM", 2)
        expected = "HELPME"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.vc = Vigenere_Cipher()

    def testGenerateOrdArray(self):
        print("\n- Vigenere_Cipher.generateOrdArray")
        result = self.vc.generateOrdArray("help me")
        expected = [7, 4, 11, 15, 12, 4]
        cetak_hasil(result.tolist(), expected)
        self.assertCountEqual(result.tolist(), expected)

    def testEncrypt(self):
        print("\n- Vigenere_Cipher.encrypt")
        result = self.vc.encrypt("help me", "lemon")
        expected = "SIXDZP"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)

    def testDecrypt(self):
        print("\n- Vigenere_Cipher.decrypt")
        result = self.vc.decrypt("SIXDZP", "lemon")
        expected = "HELPME"
        cetak_hasil(result, expected)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

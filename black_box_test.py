from Hill_Cipher import Hill_Cipher
from Rail_Fence_Cipher import Rail_Fence_Cipher
from Vigenere_Cipher import Vigenere_Cipher


def test(algo, text, key):
    print(" > Plain text :", text)
    cipher = algo.encrypt(text)
    print(" > Cipher text:", cipher)
    decrypt = algo.decrypt(cipher)
    print(" > Decryption :", decrypt)

def main():
    text = ["please help me", "we will save you"]

    key = "RRFVSVCCT"
    hc = Hill_Cipher(key)
    for i in range(2):
        print("Hill_Cipher - test case", i+1)
        test(hc, text[i], key)
        print()

    key = 3
    rfc = Rail_Fence_Cipher(key)
    for i in range(2):
        print("Rail_Fence_Cipher - test case", i+1)
        test(rfc, text[i], key)
        print()

    key = "LEMON"
    vc = Vigenere_Cipher(key)
    for i in range(2):
        print("Vigenere_Cipher - test case", i+1)
        test(vc, text[i], key)
        print()


# end def
if __name__ == "__main__":
    main()

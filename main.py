from Hill_Cipher import Hill_Cipher
from Rail_Fence_Cipher import Rail_Fence_Cipher
from Vigenere_Cipher import Vigenere_Cipher

if __name__ == "__main__":
    text = input("Please enter the message:\n> ")
    key1 = input("Please enter first key (string, 9 chars long preferred):\n> ")
    key2 = int(input("Please enter second key (integer):\n> "))
    key3 = input("Please enter third key (string):\n> ")
    is_encrypt = int(input('Please choose:\n1.Encryption\n0.Decryption\n> '))

    if is_encrypt:
        hc = Hill_Cipher(key1)
        cipher = hc.encrypt(text, key1)
        try:
            hc.decrypt(text)
            rfc = Rail_Fence_Cipher(key2)
            cipher = rfc.encrypt(cipher)
            vc = Vigenere_Cipher(key3)
            cipher = vc.encrypt(cipher)
            print(f"\nYour cipher text:\n{cipher}\nYour keys:\n{key1}, {key2}, {key3}")
        except:
            print("NB: The matrix of first key is not inverseable, try another key")
    else:
        vc = Vigenere_Cipher(key3)
        plain = vc.decrypt(text)
        rfc = Rail_Fence_Cipher(key2)
        plain = rfc.decrypt(plain)
        hc = Hill_Cipher(key1)
        plain = hc.decrypt(plain)
        print(f"\nYour plain text:\n{plain}")

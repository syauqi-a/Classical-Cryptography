import numpy as np
import re

class Vigenere_Cipher:
    def __init__(self, key:str|None = None):
        self.key = self.generateOrdArray(key.upper()) if key else None
    
    def generateOrdArray(self, text:str):
        text = re.sub(r"[^A-Z]", "", text.upper())
        text = np.array([ord(letter)-65 for letter in text], dtype=int)
        return text

    def encrypt(self, text:str, key:str|None = None):
        key = self.generateOrdArray(key) if key else self.key
        text = self.generateOrdArray(text)
        temp = np.array([text[i] + key[i%len(key)] for i in range(len(text))])
        cipher = "".join([chr(c + 65) for c in (temp % 26)])
        return cipher

    def decrypt(self, text:str, key:str|None = None):
        key = self.generateOrdArray(key) if key else self.key
        text = self.generateOrdArray(text)
        temp = np.array([text[i] - key[i%len(key)] for i in range(len(text))])
        plaintext = "".join([chr(c + 65) for c in (temp % 26)])
        return plaintext
        

def debug():
    key = "lemon"
    plain_text = "attack at dawn"
    print("Plain text:", plain_text)

    hc = Vigenere_Cipher(key)
    cipher = hc.encrypt(plain_text)
    print("Cipher text:", cipher)

    dec_text = hc.decrypt(cipher)
    print("Decryption plain text:", dec_text)


if __name__ == "__main__":
    debug()

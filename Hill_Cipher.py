import numpy as np
import re

class Hill_Chiper:
    def __init__(self, key:str):
        self.key = self.generateKeyArray(key.upper())
    
    def generateKeyArray(self, key:str):
        key = re.sub(r"[^A-Z]", "", key.upper())
        key = np.array([ord(letter)-65 for letter in key], dtype=int)
        if key.size != 9:
            print("The key's length is converted to 9 alphabetic characters")
        key.resize((3, 3), refcheck=False)
        return key

    def findDeterminant(self, key_arr):
        k = np.copy(key_arr)
        col1 = k[0][0]*((k[1][1]*k[2][2]) - (k[2][1]*k[1][2]))
        col2 = k[0][1]*((k[1][0]*k[2][2]) - (k[2][0]*k[1][2]))
        col3 = k[0][2]*((k[1][0]*k[2][1]) - (k[2][0]*k[1][1]))
        return col1 - col2 + col3

    def findAdjoint(self, key_arr):
        k = np.copy(key_arr)
        adj_key = np.eye(3, dtype=int)
        for i in range(3):
            for j in range(3):
                x = (j+1)%3
                y = (i+1)%3

                a = k[x][y] * k[(x+1)%3][(y+1)%3]
                b = k[(x+1)%3][y] * k[x][(y+1)%3]
                adj_key[i][j] = (a - b) % 26
        return adj_key

    def findInvMod(self, numb, p):
        i = 1
        r = (i*numb) % p  # get reminder
        while r != 1:
            i += 1
            r = (i*numb) % p  # get reminder
        return i

    def encrypt(self, text:str, key:str|None = None):
        # Remove non-alphabetic character and convert text into uppercase
        text = re.sub(r"[^A-Z]", "", text.upper())

        # Fill incomplate group member with Z
        n_incomplate = len(text) % 3
        text = text if n_incomplate==0 else text + ("Z"*(3-n_incomplate))

        # Convert alphabetic into integer and make array with 3 cols
        arr_text = np.array([ord(letter)-65 for letter in text.upper()],
                            dtype=int)
        arr_text = arr_text.reshape(-1, 3)

        # Encrypt the array
        temp_cipher = np.array([], dtype=int)
        key = self.generateKeyArray(key) if key else self.key
        for row in arr_text:
            temp_cipher = np.append(temp_cipher, row @ key)

        # Convert integer into alphabetic and merge them as single string
        cipher = "".join([chr(c + 65) for c in (temp_cipher % 26)])
        return cipher

    def decrypt(self, text:str, key:str|None = None):
        key = self.generateKeyArray(key) if key else self.key
        # Find inverse matrix of key
        det_key = self.findDeterminant(key)
        adj_key = self.findAdjoint(key)
        inv_key = (self.findInvMod(det_key, 26) * adj_key) % 26

        # Decrypting text by call encrypt function
        # But the key is inverse of original key
        str_key = "".join([chr(c + 65) for c in inv_key.flatten()])
        return self.encrypt(text, str_key)
        

def debug():
    key = "bravebear"
    plain_text = "kriptografi itu mudah"
    print("Plain text:", plain_text)

    hc = Hill_Chiper(key)
    cipher = hc.encrypt(plain_text)
    print("Cipher text:", cipher)

    dec_text = hc.decrypt(cipher)
    print("Decryption plain text:", dec_text)


if __name__ == "__main__":
    debug()

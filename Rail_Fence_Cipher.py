import numpy as np
import re

class Rail_Fence_Cipher:
    def __init__(self, key:int):
        self.key = key
    
    def generateOrdArray(self, text:str):
        text = re.sub(r"[^A-Z]", "", text.upper())
        text = np.array([ord(letter)-65 for letter in text], dtype=int)
        return text

    def fillingField(self, text:str, key:int):
        is_down = False
        col = 0
        row = key-1
        rail = np.array([[None for i in range(len(text))] for j in range(key)])
        for i in range(len(text)):
            is_down = True if row==0 else (False if row==key-1 else is_down)
            rail[row][col] = text[i]
            row = row+1 if is_down else row-1
            col += 1
        return rail

    def encrypt(self, text:str, key:int|None = None):
        key = key if key else self.key
        text = self.generateOrdArray(text)

        # Filling the rail field
        rail = self.fillingField(text, key)
        # Read the field and return the cipher text
        cipher = "".join([chr(c + 65) for c in rail.flatten() if c!=None])
        return cipher

    def decrypt(self, text:str, key:int|None = None):
        key = key if key else self.key
        # Marking the field
        mark = self.fillingField(np.array([True for _ in range(len(text))]), key)

        # Filling marked field
        x = 0
        for i in range(mark.shape[0]):
            for j in range(mark.shape[1]):
                if mark[i][j]:
                    mark[i][j] = text[x]
                    x += 1

        # Read the rail
        plain = ""
        is_down = False
        col = 0
        row = key-1
        for i in range(len(text)):
            is_down = True if row==0 else (False if row==key-1 else is_down)
            plain += mark[row][col]
            row = row+1 if is_down else row-1
            col += 1
        return plain
        

def debug():
    key = 4
    plain_text = "abcdefghij"
    print("Plain text:", plain_text)

    hc = Rail_Fence_Cipher(key)
    cipher = hc.encrypt(plain_text)
    print("Cipher text:", cipher)

    dec_text = hc.decrypt(cipher)
    print("Decryption plain text:", dec_text)


if __name__ == "__main__":
    debug()

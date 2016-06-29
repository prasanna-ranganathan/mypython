#!/usr/bin/env python

from Crypto.Cipher import AES

CryptoObj = AES.new("This is my key42",AES.MODE_CBC, "16 character vec")
plaintext = "This is some text we need to encrypt because it's very secret   "
ciphertext = CryptoObj.encrypt(plaintext)
print("Cipher Text: ",ciphertext)

newCryptObj = AES.new("This is my key42",AES.MODE_CBC,"16 character vec")
result = newCryptObj.decrypt(ciphertext)

print(result)

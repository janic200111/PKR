from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = os.urandom(16)
iv = os.urandom(16)

plaintext = b'Ala ma kota i psa'
plaintext = pad(plaintext, 16)

#szyfrowaniae
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = b''
prev_block = iv
for i in range(0, len(plaintext), 16):
    block = bytes([a ^ b for a, b in zip(prev_block, plaintext[i:i+16])])
    block_cipher = cipher.encrypt(block)
    ciphertext += block_cipher
    prev_block = block_cipher
#deszyfrowanie
cipher = AES.new(key, AES.MODE_ECB)
plaintext = b''
prev_block = iv
for i in range(0, len(ciphertext), 16):
    block_cipher = ciphertext[i:i+16]
    block = cipher.decrypt(block_cipher)
    plaintext += bytes([a ^ b for a, b in zip(prev_block, block)])
    prev_block = block_cipher

plaintext = unpad(plaintext, 16)
print(plaintext)
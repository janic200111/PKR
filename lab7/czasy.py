from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import time
from pathlib import Path
import matplotlib.pyplot as plt
import os
from decimal import *
getcontext().prec = 50

def encrypt_decrypt_time(tekst, key, iv, block_cipher_mode, operation):

    start_time = time.time()
    if block_cipher_mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif block_cipher_mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    elif block_cipher_mode == 'OFB':
        cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=default_backend())
    elif block_cipher_mode == 'CFB':
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    elif block_cipher_mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    
    if operation == 'encrypt':
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(tekst) + encryptor.finalize()
    elif operation == 'decrypt':
        decryptor = cipher.decryptor()
        ciphertext = decryptor.update(tekst) + decryptor.finalize()
    
    end_time = time.time()
    print( start_time, end_time)
    return Decimal(end_time - start_time)
        

tekst = Path('test.txt').read_bytes()
key = os.urandom(32)
iv = os.urandom(16)


x_values=[1000,5000,10000]
val_of_encrypt={
    'ECB':[],
    'CBC':[],
    'OFB':[],
    'CFB' : [],
    'CTR' :[]
}
val_of_decrypt={
    'ECB':[],
    'CBC':[],
    'OFB':[],
    'CFB' : [],
    'CTR' :[]
}
modess=['CTR','ECB','CBC','OFB','CFB']
for i in x_values:
    for mode in modess:
        tekst1=tekst
        for j in range(i-1):
            tekst1+=tekst
        val_of_encrypt[mode].append(encrypt_decrypt_time(tekst1,key,iv,mode,"encrypt"))
        val_of_decrypt[mode].append(encrypt_decrypt_time(tekst1,key,iv,mode,"decrypt"))
for y in val_of_encrypt:
    plt.plot(x_values, val_of_encrypt[y])
    plt.text(x_values[-1], val_of_encrypt[y][-1], "szyfrowanie")
    plt.plot(x_values, val_of_decrypt[y])
    plt.text(x_values[-1], val_of_decrypt[y][-1], "deszyfrowanie")
    plt.xlabel('Oś X')
    plt.ylabel('Oś Y')
    st = 'Czasy dla szyfrowania i deszyfrowania dla ' + y
    plt.title(st)
    plt.show()

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import time
from pathlib import Path
import matplotlib.pyplot as plt
import os

def time_of_ECB(tekst,key):

    start_time = time.time()

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(tekst, AES.block_size))

    end_time = time.time()  
    elapsed_time = end_time - start_time

    start_time = time.time()

    decryptedtext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    end_time = time.time() 
    elapsed_time1 = end_time - start_time

    return elapsed_time,elapsed_time1


tekst = Path('test.txt').read_text(encoding='utf-8')
key = os.urandom(16)
print(time_of_ECB(tekst,key))
"""
x_values=[500,2500,10000]
val={
    'md5':[],
    'sha256':[],
    'sha512':[]
}
for i in x_values:
    tekst1=""
    for j in range(i):
        tekst1+=tekst
    val['md5'].append(time_of_md5(tekst1))
    val['sha256'].append(time_of_sha256(tekst1))
    val['sha512'].append(time_of_sha512(tekst1))
print(val)

for y in val:
    plt.plot(x_values, val[y])
    plt.text(x_values[-1], val[y][-1], y)

plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Czasy dla różnych funkcji')
plt.show()
"""
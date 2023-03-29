import hashlib
import time
from pathlib import Path
import matplotlib.pyplot as plt

def time_of_md5(tekst):
    start_time = time.time()

    md5 = hashlib.md5()
    md5.update(tekst.encode())

    end_time = time.time()  

    elapsed_time = end_time - start_time

    #print(f"czas md5 dla {len(tekst)} to {'%.25f' % elapsed_time}")
    return elapsed_time

def time_of_sha256(tekst):
    start_time = time.time()

    sha256 = hashlib.sha256()
    sha256.update(tekst.encode())

    end_time = time.time()

    elapsed_time = end_time - start_time

    #print(f"czas sha256 dla {len(tekst)} to {'%.25f' % elapsed_time}")
    return elapsed_time

def time_of_sha512(tekst):
    start_time = time.time()

    sha512 = hashlib.sha512()
    sha512.update(tekst.encode())

    end_time = time.time()

    elapsed_time = end_time - start_time

    #print(f"czas sha512 dla {len(tekst)} to {'%.25f' % elapsed_time}")
    return elapsed_time

tekst = Path('test.txt').read_text(encoding='utf-8')

x_values=[100,500,1000,2000,3000,4000,5000]
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


for y_values in val.values():
    plt.plot(x_values, y_values)

# Dodanie etykiet osi X i Y oraz tytułu wykresu
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres na podstawie słownika')

# Wyświetlenie wykresu
plt.show()




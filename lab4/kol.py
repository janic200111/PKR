import hashlib
import random
def gen_tekst(len):
    wyn=""
    for i in range(len):
        wyn+=str(random.randint(0,1))
    return wyn

def get_sha(tekst):
    sha256 = hashlib.sha256()
    sha256.update(tekst.encode())
    wyn=sha256.digest()
    return ''.join(format(byte, '08b') for byte in wyn)

def get_md5(tekst):
    md5 = hashlib.md5()
    md5.update(tekst.encode())
    wyn=md5.digest()
    return ''.join(format(byte, '08b') for byte in wyn)

sr=0
for i in range(100):
    b = True
    i=0
    while b:
        tekst=gen_tekst(500)
        md=get_md5(tekst)
        sh=get_sha(tekst)
        if md[:12]==sh[:12]:
            b=False
        i+=1
    sr+=i
    print(i)
print(sr)


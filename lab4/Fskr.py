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
    return sha256.hexdigest()


encTekst = gen_tekst(100)
char = '0' if encTekst[0]=='1' else '1'
encTekst1=char+encTekst[1:]
encTekst=get_sha(encTekst)
encTekst1=get_sha(encTekst1)
k=0
print(encTekst)
print(encTekst1)

for i in range (len(encTekst1)):
    if encTekst1[i]!=encTekst[i]:
        k+=1
print(k/len(encTekst1))
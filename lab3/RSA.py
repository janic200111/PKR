import random
import numpy
def is_prime(x):
    if x<=1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def gen_prime(len,check_mod):
    rand_num=1
    min_val=10**(len-1)
    max_val=10**(len)-1
    while (not(rand_num%4==3) and check_mod) or not(is_prime(rand_num)):
        rand_num=random.randint(min_val, max_val)
    return rand_num

def eratosthenes_sieve(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False

    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)

    return primes

p=gen_prime(6,False)
q=gen_prime(6,False)
n=p*q
phi=(p-1)*(q-1)
e=0
primes=eratosthenes_sieve(100)
for i in primes:
    if numpy.gcd(i,phi)==1:
        e=i
        break
d=pow(e,-1,phi)
print(phi,n,e,d)

tekst="Szedl sasza sucha szosa"
zaszyf=[]

for i in tekst:
    c=pow(ord(i),e,n)
    zaszyf.append(c)
print(zaszyf)

deszyf=""
for i in zaszyf:
    c=pow(i,d,n)
    deszyf+=chr(c)
print(deszyf)

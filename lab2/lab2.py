import random
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

def ser_test(sign,wyn):
    licz=[0,0,0,0,0,0]
    najd_ser=0
    ser=0
    for i in range(len(wyn)):
        #print(i,ser)
        if wyn[i]==sign:
            ser+=1
            if najd_ser<ser:
                najd_ser=ser
        elif ser!=0:
            if ser<=6:
                licz[ser-1]+=1
            else:
                licz[5]+=1
            ser=0
    if ser!=0:
        if ser<=6:
            licz[ser-1]+=1
        else:
            licz[5]+=1
    print(licz)
    return najd_ser

def poker_test(wyn):
    wyst =[0]*16
    for i in range(0,len(wyn),4):
        n=int(''.join([str(x) for x in wyn[i:i+4]]),2)
        wyst[n]+=1
    sum=0
    for i in range(16):
        sum=sum + wyst[i]*wyst[i] 
    print("Test pokerowy", (16/5000)*sum-5000 )

p=gen_prime(5,True)
q=gen_prime(5,True)
n=p*q
seed=gen_prime(10,False)
print("n = ",n,"seed = ",seed)

xi=((seed*seed)%n)
wyn=[xi%2]
for i in range(20000):
    x=((xi*xi)%n)
    xi=x
    wyn.append(x%2)
#print(wyn)

num1=0
for i in wyn:
    if i==1:
        num1+=1
print("Liczba 1: ",num1)
print("Liczba 0: ",20000-num1)
print(" \nTest seri dla 1")
najd=ser_test(1,wyn)
print("Najdłuższa seria 1: ",najd)
print("\nTest seri dla 0")
najd=ser_test(0,wyn)
print("Najdłuższa seria 0: ",najd)
poker_test(wyn)



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

n=gen_prime(5,False)
g=0
for i in range(2,n):
    print(i)
    reszt=[]
    done=True
    for j in range(1,n):
        mod=pow(i,j,n)
        if mod in reszt:
            done=False
            break
        else:
            reszt.append(mod)
    if done:
        #print(reszt)
        g=i
        break
print(n,g)
x=gen_prime(5,False)
X=pow(g,x,n)
y=gen_prime(5,False)
Y=pow(g,y,n)
print(pow(X,y,n))
print(pow(Y,x,n))
    
        

            
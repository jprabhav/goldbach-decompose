import numpy as np
import time
start = time.time()


prime=np.loadtxt('primes.dat', dtype=int)
twin=np.loadtxt('twin.dat', dtype=int)
decomp=np.loadtxt('decomp.dat', dtype=int)
dtest=decomp[:100]


n=500


def f(x):        
    index=[]                                    #calculates the decomposition
    for i in range(n):
        for j in range(x):
            if (i<=j) and x==prime[i]+prime[j]:
                index.append(prime[i])
    return index
            
   
def g(x):                                       #makes the array
    l=len(f(x))
    dec=np.zeros((l,2))
    for i in range(l):
        dec[i]=f(x)[i], x-f(x)[i]
    return dec

test=np.zeros(n)
for i in range(n):
    if i==0 or i==1:
        continue
    else:
        test[i-2]=len(f(2*i))

for i in range(n):
    if test[i]==dtest[i,1]:
        print('Yes')
    else:
        print('No')

print(len(f(1240)))
    
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            
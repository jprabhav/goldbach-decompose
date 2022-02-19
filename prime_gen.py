from math import sqrt
import time
t=time.time()

prime=[2]
n=16000000h

for i in range(3,n):
    if len(prime)==1000000:
        break
    p=True
    for j in prime:
        if j>sqrt(i):
            break
        elif i%j==0:
            p=p and False
            break
    if p==True:
        prime.append(i)
           
print(len(prime))
s=time.time()
print(s-t)

file=open('milprimes.dat','w')

for i in range(1000000):                                                   
    print(prime[i],file=file)

file.close()
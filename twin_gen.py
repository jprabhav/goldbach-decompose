import numpy as np
import time
start = time.time()
twin=[]

prime=np.loadtxt('primes.dat', dtype=int)


for p in prime:
    if p+2 in prime:
        twin.append(p)
        twin.append(p+2)

'''
file=open('twinprimes.dat','w')

for i in range(1000000):                                                   
    print(twin[i],file=file)

file.close()
'''
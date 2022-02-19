import numpy as np
import time
start = time.time()

prime=np.loadtxt('primes.dat', dtype=int)
twin=np.loadtxt('twin.dat', dtype=int)

end=time.time()
print('Files loaded in', "%.4f" % (end - start)+'s.')



start = time.time()

n=10000


def f(x):                                                               #calculates the decomposition
    index=[]                                        
    for i in prime:
        if i>x/2:
            break
        for j in prime:
            if j>x:
                break
            if i<=j and x==i+j:
                index.append(i)
    
    l=len(index)
    dec=np.empty((l,2))
    for i in range(l):                                                  #puts them in an array
        dec[i]=index[i], x-index[i]
    
    return dec


test=np.empty(n)

    
'''
file=open('decompositions.dat','w')

for i in range(100):                                                    #writes the decompositions to a file
    print(2*i, '|', g(2*i).flatten(),file=file)

file.close()
'''



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            
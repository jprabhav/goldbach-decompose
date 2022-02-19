import numpy as np
import time
start = time.time()

prime=np.loadtxt('primes.dat', dtype=int)                 # list of primes
twin=np.loadtxt('twin.dat', dtype=int)                    # list of twin primes

end=time.time()
print('Files loaded in', "%.4f" % (end - start)+'s.')



start = time.time()

n=1000                                                  # the nth even integer (not including) 
                                                         # upto which we check.

def f(x):                                                # calculates the decomposition
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
    for i in range(l):                                   # puts them in an array
        dec[i]=index[i], x-index[i]
    
    d_list=dec.flatten()
    counter=0
    for i in d_list:                                     # checks for occurences of twin
        if i in twin:                                    # primes in the decompositions
            counter+=1
    return counter


test=np.empty(n)

for i in range(n):                                      
    test[i]=f(2*i)                                      #puts the occurences of twin primes in an array
    if i%500==0:
        print('Step',i)                                 # prints checkpoints 
print('Step',n)


test[0:3]=1                                             # since 0,2, and 4 are not included, we'll                                                         
                                                        # just assign 1 to the array's value.


def twin_test():
    counter=True 
    for j in test:
        if j==0:                                       # if the array has zero at any index, there are 
            counter= counter and False                 # no twin primes in the decomposition.
    print(counter)      

twin_test()


'''
#to write the decompositions to a file upto 2*n, uncomment the triple quotes.

def g(x):        
    index=[]                                    
    for i in range(n):
        for j in range(x):
            if (i<=j) and x==prime[i]+prime[j]:
                index.append(prime[i])
    l=len(index)
    dec=np.zeros((l,2))
    for i in range(l):
        dec[i]=f(x)[i], x-f(x)[i]
    return dec
            

file=open('decompositions.dat','w')

for i in range(n):                                                    
    print(2*i, '|', g(2*i).flatten(),file=file)

file.close()

'''

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            
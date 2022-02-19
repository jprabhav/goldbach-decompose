import numpy as np
import time
start = time.time()

prime=np.loadtxt('primes.dat', dtype=int)                 # list of primes

end=time.time()
print('Files loaded in', "%.4f" % (end - start)+'s.')



start = time.time()

n=10000                                                # the nth even integer (not including) 
                                                         # upto which we check.

def f(x):                                                # calculates the decomposition
    c=0                                        
    for i in prime:
        if i>x/2:
            break
        for j in prime:
            if j>x:
                break
            if i<=j and x==i+j:
                c=i
                break
    return c, x-c

print(f(20000))



'''
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

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            
import numpy as np
import time
start = time.time()

def f(x):
    return x**4 -2*x + 1

a = 0.0
b = 2.0
n = 10
h = (b-a)/n
s = (f(a) + f(b))/2
for i in range(1,n):
    s+=f(a+i*h)
    
print(s*h)

def trap(a,b,n):
    
    s=(f(a)+f(b))/2
    h=(b-a)/n
    for i in range(n):
        s += f(a+i*h)
    print(s*h)


def simp(a,b,n):
    
    s=f(a)+f(b)
    h=(b-a)/n
    for i in range(1,n,2):
        s+=4*f(a+i*h)
    
    for j in range(2,n,2):
        s+=2*f(a+i*h)
    return s*h/3

print(simp(a,b,n))
trap(a,b,n)

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            
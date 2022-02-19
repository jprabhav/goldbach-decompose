from math import sqrt
prime=[2]

n=4

for i in range(3,n):
    for j in prime:
        if i%j!=0:
            prime.append(i)
            
           



print(prime)

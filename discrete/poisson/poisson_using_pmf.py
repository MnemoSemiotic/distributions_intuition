

def factorial(n):
    if n < 0:
        # do something
        return None

    prod = 1

    for i in range(1, n+1):
        prod *= i
    
    return prod

# print(factorial(4))

from math import e
def poisson_pmf(lmbda, k):
    return (lmbda**k * e**(-lmbda)) / factorial(k)
    
''' you expect 5 people to visit your store with 10 minutes, what is the probability that 10 people visit your store in 20 minutes? lmbda = 10'''
print(poisson_pmf(10, 10))
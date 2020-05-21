

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



def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d    

for k, v in poisson_pmf_dict(lmbda=10, low_k=0, high_k30).items():
    print(f'{k}:{v}')



# ''' you expect 5 people to visit your store with 10 minutes, what is the probability that 10 people visit your store in 20 minutes? lmbda = 10'''
# print(poisson_pmf(10, 10))
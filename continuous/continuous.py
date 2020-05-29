
from math import e

def exponential_pdf(lmbda, x):
    if x < 0:
        return 0
    return lmbda * (e**(-lmbda * x))

def exponential_cdf(lmbda, x):
    if x < 0:
        return 0
    return 1 - e**(-lmbda * x)

def exponential_expectation(lmbda):
    return 1 / lmbda

def exponential_variance(lmbda):
    return 1 / lmbda**2


# print(1 - exponential_cdf(0.1, 10))

# print(exponential_expectation(0.1))

# print(exponential_variance(0.1)**(1/2))

# for time in range(0,20+1):
#     print(f'{time}: {exponential_cdf(0.1, time)}')
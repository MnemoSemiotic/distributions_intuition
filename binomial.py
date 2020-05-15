# probably of 5 successes in 20 trials, p=0.3

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

print(binomial_pmf(20, 5, 0.3))
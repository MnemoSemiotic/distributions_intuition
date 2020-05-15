# probably of 5 successes in 20 trials, p=0.3

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod


''' We can explicitly describe the probabilities in a Binomial Distribution '''

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

def binomial_dict(n, p=0.5):
    d = {}
    for k in range(0, n+1):
        d[k] = binomial_pmf(n, k, p)

    return d


def get_num_circuits_to_meet_thresh(threshold):
    '''
    returns the num_circuits in order to meet a given threshold
    '''
    
    for num_circuit_paths in range(10000):

        sum_ = 0

        for i in range(1, num_circuit_paths+1):
            sum_ += binomial_pmf(num_circuit_paths, i, (0.68))
        
            if sum_ > threshold:
                return num_circuit_paths


if __name__ == "__main__":
    # d = binomial_dict(20, 0.3)

    # for k, v in d.items():
    #     # print(f'{k}: {"*" * int(v*160)}')
    #     print(f'{k}: {v}')

    # # # breakout 1
    # # print(binomial_pmf(5, 2, 0.5)) 
    
    # # # breakout 2 pt 1
    # # print(binomial_pmf(15, 4, (7/10))) 
    
    # # # breakout 2 pt 2 
    # # sum_ = 0
    # # for i in range(0, 4):
    # #     sum_ += binomial_pmf(15, i, (7/10)) 
    # # print(sum_)

    # # # breakout 4 
    # # print(binomial_pmf(100, 25, (1/3)))

    # breakout 5 a
    print(binomial_pmf(3, 1, (0.68)))




    # breakout 5 b




print(get_num_circuits_to_meet_thresh(threshold=.99)) #-> n circuits
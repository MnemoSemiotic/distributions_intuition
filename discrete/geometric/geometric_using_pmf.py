
def geometric_pmf(p, k):
    return ((1-p)**k)*p


def geometric_cdf_closed(p, k):
    return 1 - (1-p)**(k+1)

def geometric_cdf(p, k):
    proba_ = 0

    for r in range(k):
        proba_ += geometric_pmf(p, r)
    return proba_


def geometric_pmf_dict(p, k):
    d = dict()

    for r in range(0, k+1):
        d[r] = geometric_pmf(p, r)
    
    return d

# d = geometric_pmf_dict(p=0.5, k=7)

# for k, v in d.items():
#     print(f'{k}: {v}')

def geometric_cdf_dict(p, k):
    d = dict()

    for r in range(0, k+1):
        d[r] = geometric_cdf_closed(p, r)

    return d

# d = geometric_cdf_dict(p=0.5, k=7)

# for k, v in d.items():
#     print(f'{k}: {v}')
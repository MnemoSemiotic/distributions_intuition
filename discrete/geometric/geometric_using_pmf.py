
def geometric_pmf(p, k):
    return ((1-p)**k)*p


def geometric_cdf_closed(p, k):
    return 1 - (1-p)**(k+1)

def geometric_cdf(p, k):
    proba_ = 0

    for r in range(k):
        proba_ += geometric_pmf(p, r)
    return proba_

# print(geometric_pmf(0.32, 2))


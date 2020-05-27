def geom_pmf_excl(p, k):
    # exclusive pmf
    return p*(1-p)**k

def geom_pmf_incl(p, k):
    # inclusive pmf
    return p*(1-p)**(k-1)

def geom_cdf_closed_excl(p, k):
    return 1 - (1-p)**(k+1)

def geom_cdf_closed_incl(p, k):
    return 1 - (1-p)**(k)

def geom_cdf_open(p, k, incl=True):
    proba_ = 0

    if incl==True:
        for r in range(1, k+1):
            proba_ += geom_pmf_incl(p, r)
        return proba_
    else:
        for r in range(0, k+1):
            proba_ += geom_pmf_excl(p, r)
        return proba_


# Note in these next functions, we use the exclusive forms of the geometric functions

def geometric_pmf_dict(p, k):
    d = dict()

    for r in range(0, k+1):
        d[r] = geom_pmf_excl(p, r)
    
    return d

# d = geometric_pmf_dict(p=0.5, k=7)

# for k, v in d.items():
#     print(f'{k}: {v}')

def geometric_cdf_dict(p, k):
    d = dict()

    for r in range(0, k+1):
        d[r] = geom_cdf_closed_excl(p, r)

    return d

# d = geometric_cdf_dict(p=0.5, k=7)

# for k, v in d.items():
#     print(f'{k}: {v}')
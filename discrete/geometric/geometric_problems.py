from scipy.stats import geom


'''
Geometric Breakout 1

Suppose you have an unfair coin, with a 68% chance of getting tails. 

What is the probability that the first head will be on the 3rd trial?
'''

def geom_pmf_excl(p, k):
    # exclusive pmf
    return p*(1-p)**k

def geom_pmf_incl(p, k):
    # inclusive pmf
    return p*(1-p)**(k-1)


# print(geom_pmf_excl(0.32, 2))
# print(geom_pmf_incl(0.32, 3))


# Solution: 0.147968




'''
Geometric Breakout 2

According to the article “Characterizing the Severity and Risk of Drought in the Poudre River, Colorado” taken from a water conservation journal, the drought length Y is the number of consecutive time intervals in which the water supply remains below a critical value y0 (a deficit), preceded by and followed by periods in which the supply exceeds this critical value (a surplus). The journal proposes a geometric distribution with  p = 0.409 for this random variable.

(hint: consider the probability p to represent the “success” of breaking a drought)

What is the probability that the drought lasts exactly three intervals?
'''
# print(geom_pmf_excl(0.409, 3))
# print(geom_pmf_incl(0.409, 4))

# Solution: 0.0844


'''
Given that there is a drought, what is the probability that the drought lasts at most three intervals?
'''

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


# # Note that, to answer this, we must assume that the drought is happening, so we need to subtract or omit the initial event
print(geom_pmf_excl(0.409, 3) + geom_pmf_excl(0.409, 2) + geom_pmf_excl(0.409, 1))

# print(geom_pmf_incl(0.409, 4) + geom_pmf_incl(0.409, 3) + geom_pmf_incl(0.409, 2))

# print(geom_cdf_closed_excl(0.409, 3) - geom_pmf_excl(0.409, 0))
# print(geom_cdf_closed_incl(0.409, 4) - geom_pmf_incl(0.409, 1))


# print(geom_cdf_open(0.409, 3, incl=False) - geom_pmf_excl(0.409, 0))
# print(geom_cdf_open(0.409, 4, incl=True) - geom_pmf_incl(0.409, 1))

# print(geom.cdf(4, 0.409) - geom.pmf(1, 0.409))

# # Solution: 0.469; P(Y ≤ 4) - P(Y = 1); P(Y =2) + P(Y = 3) + P(Y = 4)



'''
Geometric Breakout 3

A roulette wheel has 18 red slots, 18 black slots, and 1 green slot. It is reasonable to assume the ball is equally likely to land in any of the 37 slots.

What is the probability that the first time the ball lands in a red slot occurs on the 7th spin?
'''

p = 18/37

# print(geom_pmf_incl(p=p, k=7))
# print(geom_pmf_excl(p=p, k=6))




'''
What is the probability that the first time the ball lands in a red slot occurs sometime after the 3rd spin?
'''

print(1 - geom_pmf_incl(p=p, k=3) - geom_pmf_incl(p=p, k=2) - geom_pmf_incl(p=p, k=1))
print(1 - geom_pmf_excl(p=p, k=2) - geom_pmf_excl(p=p, k=1) - geom_pmf_excl(p=p, k=0))

print(1 - geom_cdf_closed_excl(p=p, k=2))
print(1 - geom_cdf_open(p=p, k=2, incl=False))
print(1 - geom_cdf_closed_incl(p=p, k=3))
print(1 - geom_cdf_open(p=p, k=3, incl=True))

sum_ = 0
for i in range(4, 100000):
    sum_ += geom_pmf_incl(p=(18/37), k=i)
print(sum_)

print(1 - geom.cdf(3, p))
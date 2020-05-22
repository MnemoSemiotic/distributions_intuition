

p = 0.05

from random import random

def get_bernoulli(p=0.5):
    if random() < p:
        return 1
    return 0


# for _ in range(2000):
#     flip = get_bernoulli(p)
#     if flip == 1:
#         print('SUCCESS!')
#         break
#     print(f'trial: {flip}')

def geometric(p=0.5):
    lst = []

    for _ in range(10000000000):
        trial = get_bernoulli(p)
        lst.append(trial)

        if trial == 1:
            break

    return len(lst)-1

# print(geometric(p=0.2))


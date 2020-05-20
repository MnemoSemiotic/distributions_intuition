from random import random

def bernoulli(p):
    num = random()

    if num < p:
        return True
    else:
        return False


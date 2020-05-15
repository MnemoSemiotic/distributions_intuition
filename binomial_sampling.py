from random import choice

def get_bit():
    return choice([0,1])

def generate_n_bits(n=12):
    lst = []
    for _ in range(n):
        lst.append(get_bit())
    return lst


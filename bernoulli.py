from random import choice

def bernoulli(binary_choice):
    return choice(binary_choice)

choices = [0,1]

print(bernoulli(choices))
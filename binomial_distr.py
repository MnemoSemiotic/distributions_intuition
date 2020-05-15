
def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1]

def get_binary(n_bits=8):
    bins_d = {}
    for i in range(2**n_bits):
        bins_d[i] = dec_to_bin(i, n_bits)
    return bins_d

d = get_binary()


def binomial_distr(binary_dict):
    sum_ones = dict()

    for _, v in binary_dict.items():
        successes = sum(v)
        if successes not in sum_ones:
            sum_ones[successes] = 0
        sum_ones[successes] += 1
    
    return sum_ones

binomial_dict = binomial_distr(d)

for k, v in binomial_dict.items():
    print(f'{k}: {v}')
    
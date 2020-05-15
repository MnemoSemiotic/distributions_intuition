
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

for dec, binary in get_binary().items():
    print(f'{dec}: {binary}')
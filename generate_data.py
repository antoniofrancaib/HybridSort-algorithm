import numpy as np


def generate_data(start_size=1000, end_size=1000000, max_int=101, seed=None):
    if seed is not None:
        np.random.seed(seed)

    data_sizes = []

    # we just want to take one representative value for each order of magnitude
    for exponent in range(int(np.log10(start_size)), int(np.log10(end_size)) + 1):
        size = 10 ** exponent
        data = np.random.randint(1, max_int, size)
        data_sizes.append(data)

    return data_sizes

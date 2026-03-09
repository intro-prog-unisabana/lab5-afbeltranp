def list_shift(values, shift):
    for i in range(len(values)):
        values[i] += shift


def calc_avg(values):
    return sum(values) / len(values)


def print_normalized(values):
    print(values)

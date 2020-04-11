
import numpy as np
import math


def ackley(x):
    N = x.shape[0]
    assert N == 2

    return -20 * math.e ** (0.5 * math.sqrt(sum(np.square(x)))) \
        - math.e ** (0.5 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1]))) \
        + math.e + 20

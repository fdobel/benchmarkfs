
import numpy as np
import math


def rastrigin(x):
    N = x.shape[0]
    A = 10

    return A * N + sum(x[i] ** 2 - A * math.cos(2 * math.pi * x[i]) for i in range(N))

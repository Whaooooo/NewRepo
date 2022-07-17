import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
zz = tc.gates._zz_matrix
print("zz matrix:\n", zz)
def brickwall_vtwo_layout_circuit(params, pbc=False):
    """
    `params` is for circuit trainable parameters
    """
    c = tc.Circuit(n)
    offset = 0 if pbc else 1
    for j in range(nlayers):
        for i in range(0, n - offset, 2):
            c.exp1(i, (i + 1) % n, theta=params[j, i, 2], unitary=zz)
        for i in range(n):
            c.rx(i, theta=params[j, i, 0])
        for i in range(1, n - offset, 2):
            c.exp1(i, (i + 1) % n, theta=params[j, i, 2], unitary=zz)
        for i in range(n):
            c.rx(i, theta=params[j, i, 1])
    return c
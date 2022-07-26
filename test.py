import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
import tensorcircuit as tc
c = tc.Circuit(4)
c.x(0)
c.h(1)
c.x(2)
c.z(2)
c.x(3)
c.z(3)
c.x(3)
print(c.expectation([tc.gates.x(), [0]]))
print(c.expectation([tc.gates.x(), [1]]))
print(c.expectation([tc.gates.x(), [2]]))
print(c.expectation([tc.gates.x(), [3]]))
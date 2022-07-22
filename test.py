import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
import tensorcircuit as tc
c = tc.Circuit(2)
c.x(0)
print(c.expectation([tc.gates.z(), [1]]))
print(c.expectation([tc.gates.z(), [0]]))
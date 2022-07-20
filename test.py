import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
import tensorcircuit as tc
c = tc.Circuit(2)
c.H(0)
c.H(1)
print(c.state())
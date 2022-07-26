import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
import tensorcircuit as tc
def ccc(c,i):
  y=c.X(i)
  return y
c=tc.Circuit(2)
c=ccc(c,0)
c.sample()
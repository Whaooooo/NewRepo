from tkinter import Label
from tkinter.ttk import LabeledScale
import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np
import itertools
from matplotlib import pyplot as plt
import tensorcircuit as tc
tc.set_backend("tensorflow")
X = tc.gates._x_matrix  # same as tc.gates.xgate().tensor.numpy()
Y = tc.gates._y_matrix  # same as tc.gates.ygate().tensor.numpy()
Z = tc.gates._z_matrix  # same as tc.gates.zgate().tensor.numpy()
H = tc.gates._h_matrix  # same as tc.gates.hgate().tensor.numpy()
S = tc.gates._s_matrix
T = tc.gates._t_matrix
L=3
R=3
LL=np.arange(L*(R-1)+1)
for i in range(L):
        for j in range(R-1):
            LL[i*(R-1)+j]=i*R+j
LL[L*(R-1)]=L*R
LL_new=np.delete(LL,[-1])
LLL=np.arange((L-1)*R+2)
LLL[(L-1)*R]=R*L
LLL[(L-1)*R+1]=R*L+1
LLL_new=np.delete(LLL,[-1])

c=tc.Circuit(R*L+2)
c.X(-1)
c.H(-1)
for i in range(R*L):
    c.H(i)

def oracle(c):
    for i in range(L):
        for j in range(R-1):
            c.CNOT(i*R+j+1,i*R+j)
    c.multicontrol(*LL,ctrl=[1 for _ in LL_new],unitary=X)
    for i in range(L):
        for j in range(R-1):
            c.CNOT((L-1-i)*R+(R-2-j)+1,(L-1-i)*R+(R-2-j))
    for i in range(L-1):
        for j in range(R):
            c.CNOT((i+1)*R+j,i*R+j)
    c.multicontrol(*LLL,ctrl=[1 for _ in LLL_new],unitary=X)
    for i in range(L-1):
        for j in range(R):
            c.CNOT((L-1-i)*R+(R-1-j),(L-2-i)*R+(R-1-j))
    for i in range(L):
        for j in range(R-1):
            c.CNOT(i*R+j+1,i*R+j)
    c.multicontrol(*LL,ctrl=[1 for _ in LL_new],unitary=X)
    for i in range(L):
        for j in range(R-1):
            c.CNOT((L-1-i)*R+(R-2-j)+1,(L-1-i)*R+(R-2-j))
    return c

def reflect(c):
    for i in range(R*L):
        c.H(i)
        c.X(i)
    c.multicontrol(*range(R*L),ctrl=[1 for _ in range(R*L-1)],unitary=Z)
    for i in range(R*L):
        c.X(i)
        c.H(i)
    return c

theta = math.asin(1.0/(math.sqrt(2**(R*L-1))))
r = round(((math.pi-theta) / (2 * theta)) / 2)

for _ in range(r):
    c = oracle(c)
    c = reflect(c)

c.H(-1)
c.X(-1)
print(c.sample())
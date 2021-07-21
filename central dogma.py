# rate of change of rna = Growth constant - degredation constant(gamma)*Current abundance of rna [You need mrna for them to be degraded]
# rate of change of proteins = growth constant * current abudance of mrna - degredation constant * current abbundance
# steady state = derivative = 0

import numpy as np
import matplotlib.pyplot as ply
from scipy.integrate import odeint

y0 =[5,0] #mrna and proteins
t = np.linspace(0,200,num=100) #time points
a = 0.2 #Production rate of mrna
b = 0.05 #degradation rate of mrna
c = 0.4 #production rate of proteins
d = 0.1 #degredation rate of protein

params = [a,b,c,d]

def sim(v, t, params):
    m = v[0]
    p = v[1]
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    dmdt = (a - (b * m))
    dpdt = c*m - d*p

    return([dmdt,dpdt])

o = odeint(sim, y0, t, args=(params,))
f,ax = ply.subplots(1)
line1, = ax.plot(t,o[:,0], color="b", label="Mrna")
line2, = ax.plot(t,o[:,1], color="r", label="protein")
ax.set_ylabel("abundance")
ax.set_xlabel("time")
ply.show()

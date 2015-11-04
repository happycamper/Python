#!/usr/bin/python

import numpy as np
import math
import cmath
from pylab import *


phase_offset = 0.0

wn = 0.02
zeta = 0.707
Ka = 1000.0
samples = 200
frequency_offset = 0.7

sample_arr = []
xreal = []
yreal = []
ximag = []
yimag = []
delta = []

t1 = Ka/pow(wn,2)
t2 = 2*zeta/wn

b0 = (4*Ka/t1)*(1 + t2/2.0)
b1 = (8*Ka/t1)
b2 = (4*Ka/t1)*(1 - t2/2.0)

a0 = 1.0
a1 = -2.0
a2 = 1.0

v0 = 0.0
v1 = 0.0
v2 = 0.0

phi = phase_offset
phi_hat = 0.6

x = complex(0.0,0.0)
y = complex(0.0,0.0)

print "b0: "+str(b0)+" b1: "+str(b1)+" b2: "+str(b2)
print "a0: "+str(a0)+" a1: "+str(a1)+" a2: "+str(a2)
print "index\trx\tix\try\tiy\terror"

for i in range(0,samples):
	#compute input sinusoid and update phase
	x = complex(math.cos(phi),math.sin(phi))
	phi += frequency_offset

	y = complex(math.cos(phi_hat),math.sin(phi_hat))

	(r,delta_phi) =  cmath.polar(x * y.conjugate())

	v2 = v1
	v1 = v0

	v0 = delta_phi - v1*a1 - v2*a2

	phi_hat = v0*b0 + v1*b1 + v2*b2



	xreal.append(x.real)
	ximag.append(x.imag)
	yreal.append(y.real)
	yimag.append(y.imag)
	delta.append(delta_phi)
	sample_arr.append(i)
	#print str(i)+"\t"+str(x.real)+"\t"+str(x.imag)+"\t"+str(y.real)+"\t"+str(y.imag)+"\t"+str(delta_phi)



plot(sample_arr,xreal,sample_arr,yreal)
show()
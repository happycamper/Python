#!/usr/bin/python

import numpy as np
import math as math

numIterations = 1000

tracksig = [False]*numIterations
vcofreq = np.zeros(numIterations)
ervec = np.zeros(numIterations)

count = 0
high = True

for j in range(1,numIterations):

	if(count < 4):
		if(high):
			tracksig[j] = True
		else:
			tracksig[j] = False
		count += 1
	else:
		count = 0
		if(high):
			high = False
			tracksig[j] = False
		else:
			high = True
			tracksig[j] = True

	
	#print str(tracksig[j]) + "\t" + str(count)

qsig = 0
qref = 0
lref = 0
lsig = 0
lersig = 0
phs = 0
freq = 1

prop = 1/128
deriv = 64

for i in range(1,numIterations):

	phs = (phs + math.floor(freq/pow(2,16))) % pow(2,16)
	ref = phs < 32768
	print phs
	sig = tracksig[i]

	rst = ~(qsig & qref)

	qsig = (qsig | (sig & ~lsig)) & rst
	qref = (qref | (ref & ~lref)) & rst
	lref = ref
	lsig = sig
	ersig = qref - qsig

	filtered_ersig = ersig + (ersig - lersig)*deriv

	lersig = ersig

	freq -= pow(2,16)*filtered_ersig*prop

	vcofreq[j] = freq / pow(2,16)

	ervec[j] = ersig
	#print "phs: "+str(phs)+" ref "+str(ref)+" sig "+str(sig)+" qsig "+str(qsig)

	#print vcofreq[j]
	


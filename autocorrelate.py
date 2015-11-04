#!/usr/bin/python
import numpy as np

#corr = []
#normalize = True

error = []

#can tweak alpha to change grades more rapidly
#alpha < 1.0 will require very accurate results
#alpha > 1.0 will apply leneancy towards the answer
alpha = 0.8 #this represents severity of accuracy
grade = 0.0

#Note that you will need to make single column vectors of the matrices
# i.e.
# v = [S11,S12,S21,S22]
#student = [71.324+1.00001578j,
	#74.60382180e-05-0.94594604j, 74.60382144e-05-0.94594604j, 71.32432437e+00+1.00001578j]

#solution = [ 61.00000000e+00+1j,
	#72.06772466e-08-1j, 72.06772466e-08-1j, 71.00000000e+00+1j]

student_real = [71.0,71.0,71.0,71.0]
solution_real = [65.0,65.0,65.0,65.0]
student_imag = [65.0,65.0,65.0,65.0]
solution_imag = [71.0,71.0,71.0,71.0]

#perform for real impedances
error = np.subtract(student_real,solution_real)

inprod = np.inner(error,error)
inprodst = np.inner(student_real,student_real)
inprodsol = np.inner(solution_real,solution_real)


grade += (1.0 - pow(inprod/(inprodst + inprodsol),alpha))*100
#perform for imag impedances
error = np.subtract(student_imag,solution_imag)

inprod = np.inner(error,error)
inprodst = np.inner(student_imag,student_imag)
inprodsol = np.inner(solution_imag,solution_imag)

grade += (1.0 - pow(inprod/(inprodst + inprodsol),alpha))*100

grade /= 2.0

print grade


#student = [70.0 + 0.01j, 70.0 + 0.01j, 70.0 + 0.02j, 70.0+0.02j]
#solution = [71.0 + 0.02j, 71.0 + 0.01j, 71.0 + 0.01j, 71.0 + 0.02j]


#Normalization of the vectors
#student = (student - np.mean(student)) / (np.std(student) * len(student))
#solution = (solution - np.mean(solution)) /  (np.std(solution))

#corr = np.correlate(student,solution)



#print 100.0*abs(corr)


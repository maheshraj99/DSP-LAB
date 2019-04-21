import numpy as np
import matplotlib.pyplot as plt

def disctft(a):
	a = np.asarray(a)
	l_aa = a.shape
	l_a = l_aa[0]
	print l_a
	p = np.pi
	w = np.linspace(-3.143j,3.143j,1000)
	l=1000
	y = np.zeros((l),dtype = complex)
	for k in range(l):
		s = 0
		for m in range(l_a):
			s = s+(a[m]*(np.exp(-(m*w[k]))))
		y[k]=s
	return y

M = input("filter length")
m = np.arange(0,M,1)
w_hm = 0.54-(0.46*(np.cos((2*np.pi*m)/(M-1))))
           
dw_hm = disctft(w_hm)
k = max(dw_hm)
dw_hm = dw_hm/k #normalisation
w = np.linspace(-3.143,3.143,1000)
m = 20*np.log10(np.abs(dw_hm))
plt.plot(w,m)
plt.xlabel('frequency')
plt.ylabel('magnitude in db')
plt.show()

import numpy as np
import cmath as c
j = c.sqrt(-1)
b = np.pi
def ditft(a):
	a = np.asarray(a)
	l_aa = a.shape
	la = l_aa[0]
	ww = np.arange(0,2*b,(b/100))
	l_ww = ww.shape
	l=l_ww[0]
	w = j*ww
	y = np.zeros((l),dtype=complex)
	for k in range(l):
		w_t = -1*j*w[k]
		s = 0 
		for h in range(la):
			s = s+(a[h]*np.exp(w_t*h))
		y[k] = s
	return y

a = [1,1,1]
b = ditft(a)
print b

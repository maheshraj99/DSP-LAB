import numpy as np
import matplotlib.pyplot as plt

def d_ft(a):
	a = np.asarray(a)
	l = a.shape
	n = l[0]
	ex = np.linspace(0,6.283185307j,n+1)
	#print ex
	b = np.zeros(shape=n,dtype=complex)
	for k in range(n):
			for h in range(n):
					b[k] = b[k]+(a[h]*np.exp(ex[h]*k))
		
	return (b/n)
			
a = [8,0,0,0,0,0,0,0]
b = d_ft(a)
c = np.fft.ifft(a)
b = np.abs(b)
c = np.abs(c)
print b
print c
plt.figure(1)
plt.plot(b)
plt.figure(2)
plt.plot(c)
plt.show()


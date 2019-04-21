#25/03/2019
import numpy as np
import matplotlib.pyplot as plt
import cmath

j = cmath.sqrt(-1)


def iir_butt_blt(wp,ws,delp,dels,ts): #bilinear transformation
	omcs = (2.0/ts)*(np.tan(0.5*ws))
	omcp = (2.0/ts)*(np.tan(0.5*wp))
	nc1 = np.log((((dels**(-2.0))-1.0)/((delp**(-2.0))-1.0)))
	nc2 = np.log(omcs/omcp)
	nc  = (nc1/nc2)*0.5
	n = np.ceil(nc)
	omcc = omcp/((dels**(-2)-1)**(0.5*n))
	w = np.linspace(0,3.143,100)
	h = np.zeros(shape=(100,),dtype = complex)
	if (n%2==0):
		i = 0
		for t in range(0,100):
			z = np.exp(j*w[t])
			s = (2/ts)*((1-(z**(-1)))/(1+(z**(-1))))
			s = np.abs(s)
			print s,w[t]
			m=n/2.0
			pr = 1.0
			a1 = np.arange(1,m+1)
			for k in a1:
				pr = pr*((s**2.0)+(2.0*s*omcc*np.sin(((2.0*k)-1)*3.143/n))+(omcc**2.0))
			htmp = (omcc**n)/pr
			h[i] = htmp
			i = i+1
	else:
		i = 0
		for x in w:
			s = (2.0/ts)((1.0-np.exp(-1*w[t]))/(1.0+np.exp(-1*w[t])))
			m=(n-1)/2.0
			pr = s+omcc
			a2 = np.arange(1,m+1)
			for k in a2:
				pr = pr*((s**2.0)+(2.0*s*omcc*np.sin(((2.0*k)-1)*3.143/n))+(omcc**2.0))
			htmp = (omcc**n)/pr
			h[i] = htmp
			i = i+1		
	return h



#wp = input("enter digital passband edge frq")
#ws = input("enter digital stopband start frq")
#delp = input("enter passband attenuation")
#dels = input("enter stopband attenuation")

k1 = np.empty(shape=(100,))
k2 = iir_butt_blt(1.1,2.2,0.6,0.1,0.1)
w = np.linspace(0,3.143,100)

km = np.abs(k1)
plt.plot(w,km)
plt.show()

print k1,k2


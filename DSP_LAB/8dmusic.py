import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
from scipy.io import wavfile
fs, data = wavfile.read('aaa.wav')
M = 44100*6
tau2 =-(M-1) / np.log(0.02)
window1=signal.exponential(M, 0, tau2, False)
window2=1-window1
#window1 = signal.gaussian(M, std=7)
#window2=1-window1
plt.subplot(211);plt.plot(window1);
plt.subplot(212);plt.plot(window2);plt.show()
channel1=data[:,0]#/max(abs(data[:,0]))
channel2=data[:,1]#/max(abs(data[:,1]))
#np.savetxt('channel.txt',channel1)
channel1_8d=np.zeros(len(channel1))
channel2_8d=np.zeros(len(channel1))
i=0
l=0
#channel2_8d[0:l]=channel2[0:l]
while i<=len(channel1):
	if (len(channel1[i:i+M])==44100*6):
		channel1_8d[i:i+M]=window1*channel1[i:i+M]
		channel2_8d[l:l+M]=window2*channel2[l:l+M]
	#print channel1_8d[i:i+M]
	t=window1
	window2=window1
	window1=1-window2
	l=l+44100*6
	i=i+44100*6
d_song=np.zeros((len(channel1),2))
d_song[:,0]=channel1_8d/max(abs(channel1_8d))
d_song[:,1]=channel2_8d/max(abs(channel2_8d))
plt.subplot(211);plt.plot(data[:15000,:]);
plt.subplot(212);plt.plot(d_song[:15000,:]);plt.show()
wavfile.write('8d_rb.wav', fs, d_song)


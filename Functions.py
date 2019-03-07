import math
import numpy as np
import matplotlib.pyplot as plt


def createT1 (intensity):
    return ((6*intensity)+500)/1000

def createT2(intensity):
    return ((2*intensity)+20)/1000

def decayOfZcomponent(theta,intensity,T1,time):
    theta =  theta * (math.pi / 180)
    print((theta))
    return (np.exp(-(time)/T1) * np.cos(theta) * intensity)

def decayInMxy(theta,intensity,T2,time):
    theta =  theta * (math.pi / 180)
    return (np.exp(-(time)/T2) * np.sin(theta) * intensity)

def recoveOfZcomponent(intensity,T2,time):
    return ((1- (np.exp(-(time)/T2)) )* intensity)
   

time  = np.arange(0, 50,0.001) #in millisec

pixel = 255
T1 = createT1(pixel)
T2 = createT2(pixel)
theta = 90


plt.subplot(3, 1, 1)
plt.plot(time,decayOfZcomponent(theta,pixel,T1,time))
plt.xlabel('time (s)')
plt.ylabel('Decay Mz')


plt.subplot(3, 1, 2)
plt.plot(time,decayInMxy(theta,pixel,T2,time))
plt.xlabel('time (s)')
plt.ylabel('Decay Mxy ')

plt.subplot(3, 1, 3)
plt.plot(time,recoveOfZcomponent(pixel,T2,time))
plt.xlabel('time (s)')
plt.ylabel('Recovery of X component')

plt.show()


 
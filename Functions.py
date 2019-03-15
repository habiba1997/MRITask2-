import math
import numpy as np
import matplotlib.pyplot as plt

def createPD(intensity):
    return (1/255)*intensity 

def createT1 (intensity):
    return ((6*intensity)+500)/1000

def createT2(intensity):
    return ((2*intensity)+20)/1000

def rotationAroundYaxisMatrix(theta,vector):
    vector = vector.transpose()
    theta = (math.pi / 180) * theta
    R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
    R = np.dot(R, vector)
    R = R.transpose()
    return np.matrix(R)

def recoveryDecayEquation(T1,T2,PD,vector):
    vector = vector.transpose()
    Decay =  []
    Rec = []
    for i in range(len(time)):
        Decay = np.append(Decay,np.dot([[np.exp(-time[i]/T2),0,0],[0,np.exp(-time[i]/T2),0],[0,0,np.exp(-time[i]/T1)]],vector))
        Rec =  np.append(Rec, np.dot([[0,0,(1-(np.exp(-time[i]/T1)))]],PD) )
    
    Decay = np.matrix(Decay)
    Rec =  np.matrix(Rec)
    RD  = Decay + Rec
    RD = RD.reshape(len(time),3)
    RD = RD.transpose()
   
    return RD


time  = np.arange(0, 10,0.001) #in sec but step in 1 msec
#print(time)
vector= np.matrix ([0,0,1])

pixelIntensity = 200
theta = 90
T1 = createT1(pixelIntensity)
T2 = createT2(pixelIntensity)
PD = createPD(pixelIntensity)

vector = rotationAroundYaxisMatrix(theta,vector)
RecoveryDecayMatrix = (recoveryDecayEquation(T1,T2,PD,vector))
x = RecoveryDecayMatrix[0,:]
print(x)
print(x.shape)
y = np.array(RecoveryDecayMatrix[0,:]).ravel()
print(y)
print(type(y))

"""array = [1 ,2 ,3 ,4,5]
print(type(array))
print("done")
plt.subplot(3, 1, 1)
plt.plot(time,RecoveryDecayMatrix[:,0])
plt.xlabel('time (s)')
plt.ylabel('Decay Mx')

plt.subplot(3, 1, 2)
plt.plot(time,RecoveryDecayMatrix[:,1])
plt.xlabel('time (s)')
plt.ylabel('Decay My ')

plt.subplot(3, 1, 3)
plt.plot(time,RecoveryDecayMatrix[:,2])
plt.xlabel('time (s)')
plt.ylabel('Recovery Z')

plt.show()"""

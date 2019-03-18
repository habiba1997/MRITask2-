
import numpy as np
import math

def rotationAroundYaxisMatrix(theta,vector):
        vector = vector.transpose()
        theta = (math.pi / 180) * theta
        R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
        R = np.dot(R, vector)
        R = R.transpose()
        return np.matrix(R)


def rotationAroundZaxisMatrixXY(TR,speed,vector,time): #time = self.time
        vector = vector.transpose()
        theta = speed * (time/ TR)* time
        theta = (math.pi / 180) * theta
        XY = np.matrix([[np.cos(theta),-np.sin(theta),0], [np.sin(theta), np.cos(theta),0],[0, 0, 1]])
        XY = np.dot(XY,vector)
        XY = XY.transpose()
        return np.matrix(XY) 


def recoveryDecayEquation(T1,T2,PD,vector,time):
        vector = vector.transpose()
        Decay =np.matrix([[np.exp(-time/T2),0,0],[0,np.exp(-time/T2),0],[0,0,np.exp(-time/T1)]])
        Decay = np.dot(Decay,vector)
     
        Rec= np.dot(np.matrix([[0,0,(1-(np.exp(-time/T1)))]]),PD)
        Rec = Rec.transpose()
        Decay = np.matrix(Decay)
        Rec =  np.matrix(Rec)    
     
        RD  = Decay + Rec
        RD = RD.transpose()
        return RD

vector= np.matrix ([0,0,1]) #da range sabt
T1 =2
T2 =0.5
time =0.5
PD = 1
Tr =2
speed = 1
theta =90 

"""print(" ")
vector = rotationAroundYaxisMatrix(theta,vector)
print("rotationAroundYaxisMatrix:       " , vector)

print(" ")

vector = rotationAroundZaxisMatrixXY(Tr,speed,vector,time)
print("rotationAroundZaxisMatrixXY:     ", vector)

print(" ")

vector = recoveryDecayEquation(T1,T2,PD,vector,time)
print("recoveryDecayEquation:    " ,vector)
"""
print(vector.item(2))
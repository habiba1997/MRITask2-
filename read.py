

import numpy as np 
import math


def rotationAroundYaxisMatrix(theta,vector):
            vector = vector.transpose()
            theta = (math.pi / 180) * theta
            R = ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
            R = np.dot(R, vector)
            R = R.transpose()
            return R

x = np.matrix([0,0,1])


import pprint
n = 3
distance = [[[0 for k in range(3)] for j in range(4)] for i in range(4)]

for i in range(4):
        for j in range(4):
                distance[i][j] = rotationAroundYaxisMatrix(90,x)
                vector = np.matrix([0,0,1])
                vector= np.ravel(distance[i][j]* vector.transpose())
                distance[i][j] = [[0,0,vector[0]]]

for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                totalTheta = complex(GyStep,GxStep)
                x = np.ravel(signal[i][j])[0]
                y = np.ravel(signal[i][j])[1]
                z = math.sqrt( (x*x) + (y*y) )
                #print("Before || Kspace= ", Kspace) 
                #print(np.exp(complex(0,totalTheta)))
                Kspace[Ki,Kj]= Kspace[Ki,Kj]+ (z * np.exp(complex(0,totalTheta)))
                #print("After || Kspace= ", Kspace) 

"""
        x = 0
        y = 0 
        
        for i in range(len(signal)):
            for j in range(len(signal)):
                signal[i][j] = rotationAroundZaxisMatrixXY(GxStep,np.matrix(signal[i][j]))
                signal[i][j] = rotationAroundZaxisMatrixXY(GyStep,np.matrix(signal[i][j]))
                                
                x = x + np.ravel(signal[i][j])[0]
                y = y + np.ravel(signal[i][j])[1]
        
        Kspace[Ki,Kj]= complex(x,y)          
"""        

"""
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                print("signal: ", signal[i][j])
                totalTheta = complex(GyStep,GxStep)
                print("totalTheta: ", totalTheta)
                z = abs(complex(np.ravel(signal[i][j])[0],np.ravel(signal[i][j])[1]))
                print("Before || Kspace= ", Kspace) 
                print("absolute:",z* np.exp(complex(0,totalTheta)))
                Kspace[Ki,Kj]= Kspace[Ki,Kj] + (float)(z * np.exp(complex(0,totalTheta)))
                print("After || Kspace= ", Kspace) 
"""
    
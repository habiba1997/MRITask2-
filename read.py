

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

start = False

if start:
        print("false")
else:
        pprint.pprint(distance)
        
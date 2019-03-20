import numpy as np
import math
from matplotlib import pyplot as plt

#Generate random array of zeros 512 rows and 512 columns

img = np.zeros((512,512))
T1 = np.zeros((512,512))
T2 = np.zeros((512,512))
#create white box an array [value] is the no. of values and determine the intensity, reshape it into rows and columns

box1 = np.array([25]*70*50).reshape(70,50)
box2 = np.array([200]*25*150).reshape(25,150)
box3 = np.array([120]*100*25).reshape(100,25)
box4 = np.array([255]*100*50).reshape(100,50)
box5 = np.array([100]*50*70).reshape(50,70)

#Generate specific x-y coordinates 
x1=250
y1=250
x2=290
y2=290
x3=240
y3=285
x4=210
y4=220
x5=310
y5=305

#Replace part of original image with white box

img[x1:x1+70, y1:y1+50] = box1
img[x2:x2+25, y2:y2+150] = box2
img[x3:x3+100, y3:y3+25] = box3
img[x4:x4+100, y4:y4+50] = box4
img[x5:x5+50, y5:y5+70] = box5






# a function that returns T1 ( recovery time ) based on the intensity
def createT1(intensity):

    if intensity == 100: #Gray matter
        T1=900
        
    elif intensity == 255: #white matter
        T1= 510
       
    elif intensity == 200: #muscle
        T1=900
       
    elif intensity == 120 : #fat
        T1=300
        
    elif intensity == 25: #protein
        T1=250
        
    #elif intensity == 0: #Black => air
    #    T1=1
        
    else: # general case for any phantom whatever its intensity 
        T1 = (7.5*intensity) + 50

    return T1

def createPD(intensity):
        return (1/255)*intensity 

# a function that returns T2 ( decay time ) based on the intensity
def createT2(intensity):

    if intensity == 100: #Gray matter
        T2 =90
   
    elif intensity == 255: #white matter       
        T2 =70

    elif intensity == 200: #muscle        
        T2 = 50

    elif intensity == 120 : #fat        
        T2 = 100

    elif intensity == 25: #protein       
        T2 = 30

    #elif intensity == 0: #Black => air        
    #    T2=0

    else: # general case for any phantom whatever its intensity 
        T2 = 0.5*intensity+10

    return T2





def rotationAroundYaxisMatrix(theta,vector):
            vector = vector.transpose()
            theta = (math.pi / 180) * theta
            R = np.matrix ([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]] )
            R = np.dot(R, vector)
            R = R.transpose()
            return np.matrix(R)


def rotationAroundZaxisMatrixXY(TR,speed,vector,time): #time = self.time
            vector = vector.transpose()
            theta = speed * (time/ TR)
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




"""
for i in range(self.img.shape[0]):
    for j in range(self.img.shape[1]):
        T1[i,j]=createT1(self.img[i,j])
        T2[i,j]=createT2(self.img[i,j])
"""
import pprint
TE = 0.1
vector= np.matrix ([0,0,1]) #da range sabt
theta = 90 
TR = 1
Kspace = [[[0 for k in range(3)] for j in range(img.shape[0])] for i in range(img.shape[1])]

signal = [[[0 for k in range(3)] for j in range(img.shape[0])] for i in range(img.shape[1])]

start = True

for Ki in range(len(Kspace)):
    #move in each image pixel
    print('Ki: ',Ki)
    if start :
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                vectorNew = np.dot(vector , createPD(img[i,j]) )
                signal[i][j] =  rotationAroundYaxisMatrix(theta,vectorNew)
                signal[i][j] =  signal[i][j] * np.exp(-TE/createT2(img[i,j]))
    else:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                signal[i][j] =  rotationAroundYaxisMatrix(theta,signal[i][j])
                signal[i][j] =  signal[i][j] * np.exp(-TE/createT2(img[i,j]))
    # for kspace column
    for Kj in range (len(Kspace)):
        print('Kj: ',Kj)
        GxStep = ((2 * math.pi) / len(Kspace)) * Ki
        GyStep = ((2 * math.pi) /len(Kspace)) * Kj
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                totalTheta = complex(GyStep,GxStep)
                Kspace[Ki][Kj]+=signal[i][j] * np.exp(complex(0,totalTheta))
    
    for i in range(img.shape[0]):
        print("recover")
        for j in range(img.shape[1]):
            signal[i,j] = recoveryDecayEquation(createT1(img[i,j]),createT2[i,j],createPD[i,j],signal[i][j],TR)
            vector = np.matrix([0,0,1])
            vector= np.ravel(signal[i][j]* vector.transpose())
            signal[i][j] = [[0,0,vector[0]]]

print(Kspace)

    






#print(img.shape)
plt.imshow(img, cmap="gray")
plt.show()
plt.imshow(T1, cmap="gray")
plt.show()
plt.imshow(T2, cmap="gray")
plt.show()



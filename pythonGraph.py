
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image

#Generate random array of zeros 512 rows and 512 columns

img = np.zeros((512,512))

#create white box an array [value] is the no. of values and determine the intensity, reshape it into rows and columns

box1 = np.array([255]*200*200).reshape(200,200)
box2 = np.array([150]*125*125).reshape(125,125)
box3 = np.array([125]*125*125).reshape(125,125)
box4 = np.array([50]*250*250).reshape(250,250)
box5 = np.array([200]*300*300).reshape(300,300)

#Generate specific x-y coordinates 

x1=50
y1=50
x2=300
y2=10
x3=10
y3=10
x4=120
y4=120
x5=212
y5=212

#Replace part of original image with white box

img[x1:x1+200, y1:y1+200] = box1
img[x2:x2+125, y2:y2+125] = box2
img[x3:x3+125, y3:y3+125] = box3
img[x4:x4+250, y4:y4+250] = box4
img[x5:x5+300, y5:y5+300] = box5

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
        
    elif intensity == 0: #Black => air
       T1=0
        
    else: # general case for any phantom whatever its intensity 
        T1 = (7.5*intensity) + 50

    return T1


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

    elif intensity == 0: #Black => air        
       T2=0

    else: # general case for any phantom whatever its intensity 
        T2 = 0.5*intensity

    return T2


def mappingT1 (T1): #T1 in msec assumption
        return (T1-500)/6

def mappingT2 (T2):  #T1 in msec assumption
        return (T2-20)/2

T1 = np.zeros((512,512))
T2= np.zeros((512,512))


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        T1[i,j]=mappingT1(createT1(img[i,j]))
        T2[i,j]=mappingT2(createT2(img[i,j]))


import scipy.io

output = {
		"Phantom" : img,
        "T1": T1,
        "T2":T2,
	}
scipy.io.savemat('phantomTwo', output)



plt.imshow(img, cmap="gray")
plt.show()
import numpy as np

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


T1 = np.zeros((512,512))
T2= np.zeros((512,512))


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        T1[i,j]=createT1(img[i,j])
        T2[i,j]=createT2(img[i,j])


import scipy.io

output = {
		"Phantom" : img,
        "T1": T1,
        "T2":T2,
	}
scipy.io.savemat('phantomOne', output)






plt.imshow(img, cmap="gray")
plt.show()



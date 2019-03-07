
import numpy as np

from matplotlib import pyplot as plt

#Generate random array of zeros 512 rows and 512 columns

img = np.zeros((512,512))

#create white box an array [value] is the no. of values and determine the intensity, reshape it into rows and columns

box1 = np.array([255]*50*50).reshape(50,50)
box2 = np.array([150]*25*25).reshape(25,25)
box3 = np.array([125]*25*25).reshape(25,25)
box4 = np.array([50]*50*50).reshape(50,50)
box5 = np.array([200]*30*30).reshape(30,30)

#Generate specific x-y coordinates 

x1=250
y1=250
x2=290
y2=290
x3=240
y3=285
x4=220
y4=220
x5=300
y5=310

#Replace part of original image with white box

img[x1:x1+50, y1:y1+50] = box1
img[x2:x2+25, y2:y2+25] = box2
img[x3:x3+25, y3:y3+25] = box3
img[x4:x4+50, y4:y4+50] = box4
img[x5:x5+30, y5:y5+30] = box5

#plot in gray scale

plt.imshow(img, cmap="gray")
plt.show()



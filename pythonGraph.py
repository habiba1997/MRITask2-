
import numpy as np

from matplotlib import pyplot as plt

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

#plot in gray scale

plt.imshow(img, cmap="gray")
plt.show()



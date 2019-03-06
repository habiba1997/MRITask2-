from PIL import Image
import numpy as np

from matplotlib import pyplot as plt

#Generate random array of zeros 512 rows and 512 columns
img = np.zeros((512,512))

#Make white box an array 255 values bt3to *50 *50 y3ny mt3ada 2500 mara w reshape bt reshape it into rows and columns
box = np.array([255]*50*50).reshape(50,50)

#Generate random coordinates of x and y 
x, y = np.random.randint(0,512-5, size=2)

#Replace part of original image with white box
img[x:x+50, y:y+50] = box

plot BUT IN grey scale
plt.imshow(img, cmap="gray")
plt.show()

#imga = Image.fromarray(img, 'L')
#imga.save('my.png')
#imga.show()

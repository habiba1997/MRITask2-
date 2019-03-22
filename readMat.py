import scipy.io as sio
from matplotlib import pyplot as plt
#Check Line 93 on phantom2.py 


output = sio.loadmat ('phantomOne.mat')

img = output['Phantom']
T1 = output['T1']
T2 = output['T2']

plt.imshow(img, cmap="gray")
plt.show()
plt.imshow(T1, cmap="gray")
plt.show()
plt.imshow(T2, cmap="gray")
plt.show()
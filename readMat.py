import scipy.io as sio
from matplotlib import pyplot as plt
#Check Line 93 on phantom2.py 

"""
import scipy.io
output = {
		"iphone" : img
	}
scipy.io.savemat('phantomOne', output)
"""

output = sio.loadmat ('E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantomOne.mat')

img = output['iphone']

plt.imshow(img, cmap="gray")
plt.show()
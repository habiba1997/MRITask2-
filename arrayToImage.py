import matplotlib.pyplot as plt
import numpy as np
     
X = np.random.random((100, 100)) # sample 2D array
plt.imshow(X, cmap="gray")
plt.show()
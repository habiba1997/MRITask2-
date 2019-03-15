
from matplotlib import pyplot as plt
import numpy as np
from imageio import imsave, imread
from PIL import Image

bd = np.matrix([[44., -1., 40., 42., 40., 39., 37., 36., -1.],
                [42., -1., 43., 42., 39., 39., 41., 40., 36.],
                [37., 37., 37., 35., 38., 37., 37., 33., 34.],
                [35., 38., -1., 35., 37., 36., 36., 35., -1.],
                [36., 35., 36., 35., 34., 33., 32., 29., 28.],
                [38., 37., 35., -1., 30., -1., 29., 30., 32.]])

plt.imshow(bd, cmap="gray")
plt.show()
bd = bd.astype(np.uint8)
imsave("E:\Study\Third year\Second Term\MRI\Task2\Task2\MRITask2-\phantom2.png", bd)
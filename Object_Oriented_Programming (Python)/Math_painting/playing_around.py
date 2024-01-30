import numpy as np
from PIL import Image

data = np.zeros((10,8,3),dtype=np.uint8)
data[:] = [220, 220,50]
print(data)

#data[1:3] = [220, 100,50]
data[1:6,1:3] = [100, 100,50]
data[5:7,3:5] = [200, 10,150]


img = Image.fromarray(data, 'RGB')
img.save('files/test.png')


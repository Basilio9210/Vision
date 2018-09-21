# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:24:28 2018

@author: BASILIO.SALDARRIAGA
"""

from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters

Im_g = Image.open('Penguins.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")
plt.title("imagen original")


Im_f1 = filters.uniform_filter(Im_ga, 15)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme")


Im_f1 = filters.gaussian_filter(Im_ga, 15)
#Im_f1 = filters.uniform_filter(Im_ga, 10)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro gaussiano")
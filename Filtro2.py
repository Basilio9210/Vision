# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:33:17 2018

@author: BASILIO.SALDARRIAGA
"""


from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters
import funcion_mse as fun


Im_g = Image.open('Penguins.jpg').convert('L')
Im_ga = np.array(Im_g)

plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

[row, col] = Im_ga.shape;
Im_n = np.double(Im_ga)
for i in range(0, row-1):
    for j in range(0, col-1):
        Im_n[i,j] = Im_n[i, j] + np.random.uniform(0, 100)

plt.gray()
plt.imshow(Im_n)
plt.axis("off")
plt.title("imagen")

Im_f1 = filters.uniform_filter(Im_n, 0.07)
mse = fun.my_mse(Im_ga, Im_f1)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme")

Im_f2 = filters.gaussian_filter(Im_n, 0.07)
mse = fun.my_mse(Im_ga, Im_f2)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("mse")

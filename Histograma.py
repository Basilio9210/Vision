# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:09:50 2018

@author: BASILIO.SALDARRIAGA
"""

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Vision')
#import Funciones as trans

def my_histograma(im):
    [row, col] = im.shape;
    vec = np.zeros(256)
    print(vec.shape)
    for i in range(0, row-1):
        for j in range(0, col-1):
            valor = im[i, j]
            vec[valor] = vec[valor] + 1
        return vec
    

Im_g = Image.open('bears.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")

h = my_histograma(Im_ga)
plt.figure()
plt.bar(np.arange(256), h)

#Ecualizacion de la imagen.

h2 = my_histograma(Im_ga)
plt.figure()
plt.bar(np.arange(256), h2)

plt.gray()
plt.imshow(h2)
plt.axis('off')
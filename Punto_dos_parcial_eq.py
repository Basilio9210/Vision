# Basilio Saldarriaga
"""
Created on Mon Sep  3 18:24:29 2018


Created on Wed Aug 22 19:09:50 2018

@author: BASILIO.SALDARRIAGA



1. Pasar la imagen a escala de grises

2. Calcular el histograma de la imagen en escala de grises 

3. Realizar la ecualización del histograma de la imagen en escala de grises

4. Gráficar en una figura: la imagen en escala de grises original, la imagen ecualizada,
   el histograma original y el histograma ecualizado 

"""

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\Vision')
#import Funciones as trans



def my_equal(im, h):
    [row, col] = im.shape;
    n = row * col
    p = h/n
    s = np.cumsum(p)
    k = s * 255
    im2 = im
    for i in range(0, row-1):
        for j in range(0, col-1):
            valor = im[i, j]
            im2[i, j] = k[valor]
        return im2


Im_g = Image.open('imagen_dos_quiz.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")


#Ecualizacion de la imagen.

eq = my_equal(Im_ga)
plt.figure()
plt.bar(np.arange(256), eq, color = 'green')


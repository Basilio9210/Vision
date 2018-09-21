# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:32:20 2018

@author: BASILIO.SALDARRIAGA
"""

from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
import FuncionesFiltros as fun

Im_g = Image.open('BuildSaltPepper.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")
plt.title("imagen original")


I_median = fun.my_medianfilter(Im_ga)
plt.figure()  
plt.gray()
plt.imshow(I_median)
plt.axis("off")
plt.title("filtro mediano")

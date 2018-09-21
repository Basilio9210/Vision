# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:04:23 2018

@author: BASILIO.SALDARRIAGA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:32:20 2018

@author: BASILIO.SALDARRIAGA
"""

from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
import FuncionesFiltros as fun

Im_g = Image.open('building.jpg').convert('L')
Im_ga = np.array(Im_g)
plt.gray()
plt.imshow(Im_ga)
plt.axis("off")
plt.title("imagen original")


[Ig, Ix, Iy] = fun.my_gradient(Im_ga)
plt.figure()  
plt.gray()
plt.imshow(Ix)
plt.axis("off")
plt.title("derivda en x")

plt.figure()  
plt.imshow(Iy)
plt.axis("off")
plt.title("derivda en y")

plt.figure()  
plt.imshow(Ig)
plt.axis("off")
plt.title("gradiente")


#Punto E
If_unif

If_gaus
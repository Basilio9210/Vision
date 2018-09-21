from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('E:/2018-2/VA') #esta linea toma los archivos desde la USB
import tranformacion_lineal as trans

Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.array(Im_g)
Im2 = trans.my_gamma( Im_ga, 0.3) #aca se manda la imagen  y el valor para el exponente Y al metodo
#RECUERDE SI LA IMAGEN ES MUY CLARA Y>1 SI ES OSCURA Y<1, EN ESTE CASO Y VALE 2
plt.gray()
plt.imshow(np.uint8(Im_ga)) # esta linea no es necesaria ya se esta transformado en my_gamma
plt.axis('off')
plt.figure()
plt.gray()
plt.imshow(Im2)
plt.axis('off')

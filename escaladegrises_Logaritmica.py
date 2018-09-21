from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

Im_g = Image.open('img2.jpg').convert('L')
Im_ga = np.double(np.array(Im_g)) #pasa el formato a double para no perder precision
Im2 = np.log(1+Im_ga) #Log imagen, se le suma a los valores cero 1
Im2 = np.uint8(255*Im2/Im2.max())
 #escala de nuevo a los enteros 
plt.gray()#las siguientes tres lineas muestran la img original
plt.imshow(np.uint8(Im_ga))
plt.axis("off")

plt.figure() #muestra la imagen con el log
plt.gray()
plt.imshow(Im2)
plt.axis("off")
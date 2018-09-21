# BASILIO SALDARRIAGA 
# ANDERSON HERRERA

"""
a.Escriba una función en que implemente la transformación gamma de una imagen en escala de grises. La
 función debe recibir como parámetros de entrada: una imagen en escala de grises (uint8) y el parámetro
 gamma . El parámetro de salida de la función debe ser una imagen en escala de grises (uint8). Para ϒ
 evitar perder precisión en el cálculo de los valores de niveles de grises, convierta la imagen a double
 antes de calcular la transformación gamma. La imagen debe convertirse nuevamente a uint8 antes de
 retornar de la función.
 
b. Seleccione una imagen a color y aplique la transformación gamma 
para Y=0.05, 0.10, 0.20, 0.50, 1, 1.5,2.5, 5.0, 10.0, 25.0.

"""

from PIL import Image #importe de libreria PIL
import numpy as np #importe de libreria numpy
import matplotlib.pyplot as plt #importe de libreria matplotlib
import sys #improte de libreria SYS

sys.path.append('D:\Vision')  #la ruta de los archivos USB
import tranformacion_lineal as trans # importe de libreria
Im_g = Image.open('bears.jpg').convert('L') #importa la libreria IMAGE para abrir la imagen
Im_ga = np.double(np.array(Im_g)) #Transofrmacion de la imagen a DOUBLE
Im2 = trans.my_gamma( Im_ga, 25.0) #Aca se manda la imagen  y el valor para el exponente al metodo para Y=0.05, 0.10, 0.20, 0.50, 1, 1.5,2.5, 5.0, 10.0, 25.0.
plt.gray() #la libreria matplotlib convierte la imagen a gris

plt.imshow(np.uint8(Im_ga)) # esta linea no es necesaria ya se esta transformado en my_gamma
plt.axis('off') #no muestra los ejes en la terminal
plt.figure()# realiza la grafica

plt.gray() #la libreria matplotlib convierte la imagen a gris
plt.imshow(Im2)#guarda la imagen
plt.axis('off') #no muestra los ejes en la terminal


Im2 = Image.fromarray(Im2, mode="L")  #importa la libreria IMAGE para abrir la imagen
Im2.save("D:/Vision/Taller 1/Punto1/result8.jpg") #guardamos la imagen en la ruta de la usb

plt.gray() #la libreria matplotlib convierte la imagen a gris
plt.imsave(Im2) #guarda la imagen
plt.axis('off') #no muestra los ejes en la terminal


#Im2.save(Im2)

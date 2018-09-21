"""
1. Cargar la imagen en Python

2. Transformar la imagen a escala de grises, visualizar en una figura la imagen original y la imagen en escala de grises 

3. Aplique la transformada gamma. Seleccione el parametro gamma de tal forma que permita oscurecer la imagen y ver mejor los detalles. 

Para este punto puede usar las funciones realizadas en clase y en los talleres. Envie al correo mariatorres@itm.edu.co en una carpeta comprimida el programa en matlab, las funciones empleadas y la imagen. 

Para finalizar marque True.


"""
#BASILIO SALDARRIAGA

from PIL import Image #importe de libreria PIL
import numpy as np #importe de libreria numpy
import matplotlib.pyplot as plt #importe de libreria matplotlib
import sys #improte de libreria SYS

sys.path.append('D:\Vision')  #la ruta de los archivos USB
import tranformacion_lineal as trans # importe de libreria
Im_g = Image.open('imagen_uno_quiz.jpg').convert('L') #importa la libreria IMAGE para abrir la imagen
Im_ga = np.double(np.array(Im_g)) #Transofrmacion de la imagen a DOUBLE
Im2 = trans.my_gamma( Im_ga, 20) #Aca se manda la imagen  y el valor para el exponente al metodo para Y=0.05, 0.10, 0.20, 0.50, 1, 1.5,2.5, 5.0, 10.0, 25.0.
plt.gray() #la libreria matplotlib convierte la imagen a gris

plt.imshow(np.uint8(Im_ga)) # esta linea no es necesaria ya se esta transformado en my_gamma
plt.axis('off') #no muestra los ejes en la terminal
plt.figure()# realiza la grafica

plt.gray() #la libreria matplotlib convierte la imagen a gris
plt.imshow(Im2)#guarda la imagen
plt.axis('off') #no muestra los ejes en la terminal


Im2 = Image.fromarray(Im2, mode="L")  #importa la libreria IMAGE para abrir la imagen
Im2.save("D:/Vision/Parcial/Punto_1/imagen_uno_quiz_en_gamma_8.jpg") #guardamos la imagen en la ruta de la usb


plt.gray() #la libreria matplotlib convierte la imagen a gris
plt.imsave(Im2) #guarda la imagen
plt.axis('off') #no muestra los ejes en la terminal


#Im2.save(Im2)

# BASILIO SALDARRIAGA 
# ANDERSON HERRERA


"""
a. Escriba una función que permita resaltar un rango de grises específico en una imagen. La función debe
recibir como parámetros de entrada: una imagen en escala de grises (uint8), el parámetro A y B que
define el rango de valores que la función va a resaltar. A y B deben ser positivo y menores a 255. La
imagen de salida será una imagen en blanco y negro; los pixeles blancos corresponderán a los pixeles
con valores entre A y B en la imagen de entrada, y los pixeles negros a todos los demás pixeles.


b. Seleccione una imagen a color, transforme la imagen a escala de grises y aplique el realce de rango de
grises para los siguientes valores de A y B: [A, B] = {[20 240], [40 200], [80 180], [100 150], [120 135]}. 
"""


from PIL import Image #importe de libreria PIL
import matplotlib.pyplot as plt #importe de libreria matplotlib


def resaltar(imagen, rango): #funcion para resaltar la imgen, crear un rango y recorrer los pixeles
    x, y = rango
    pixels = imagen.load()
    w, h = imagen.size # tamaño de la imagen.
    for i in range(w):
        for j in range(h):
            pixels[i, j] = 0 if  x <= pixels[i, j] <= y else 255 #operacion que va de 0 a 255 lo que permite mostrar las partes en grises mas reslatadas.


image_rgb= Image.open('Tulips.jpg').convert('L') # Convierte la imagen a escala de gris
image_gray = image_rgb.convert('L') #Operacion para escalar la iimagen nuevamente
resaltar(image_gray,[20, 240]) # [A, B] = {[20 240], [40 200], [80 180], [100 150], [120 135]}.
plt.imshow(image_rgb) #muestra la imagen_rgb
plt.show() #grafica


plt.imshow(image_gray) #grafica
image_gray.save("D:/Vision/Taller 1/Punto2/resultado4.jpg") # guardamos la imagen D:\Vision\Taller 1\Punto2
plt.gray() #grafica
plt.axis("off") #para q no muestre el plano cartesiano 





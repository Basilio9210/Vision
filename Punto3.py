# BASILIO SALDARRIAGA
# ANDERSON HERRERA

"""

PROBLEMA 3: REALCE DE RANGO DE GRISES

a. Repita el problema anterior para una función que resalte los pixeles dentro del rango [A,B] y preserve el
resto de pixeles. En este caso la imagen de salida será una imagen en escala de grises (uint8), donde los
pixeles con valores entre A y B en la imagen original serán blancos, y todos los demás preservarán su
valor inicial.

b. Seleccione una imagen a color, transforme la imagen a escala de grises y aplique la segunda versión del
realce de rango de grises para los siguientes valores de A y B: [A, B] = {[20 240], [40 200], [80 180],
[100 150], [120 135]}.

"""


from PIL import Image #importe de libreria PIL
 #importe de libreria numpy
import matplotlib.pyplot as plt #importe de libreria matplotlib


def resaltar(imagen, rango):
    x, y = rango
    pixels = imagen.load()
    w, h = imagen.size
    for i in range(w):
        for j in range(h):
            pixels[i, j] = pixels[i, j] if  x <= pixels[i, j] <= y else 255 #operacion para asignar rango de lo que lleva el valor del pixel  hasta 255



image_rgb= Image.open('Koala.jpg').convert('L') # Convierte la imagen a escala de gris
image_gray = image_rgb.convert('L') #Operacion para escalar la iimagen nuevamente
resaltar(image_gray,[120, 135]) # [A, B] = {[20 240], [40 200], [80 180], [100 150], [120 135]}.
plt.imshow(image_rgb) #muestra la imagen_rgb
plt.show() #grafica


plt.imshow(image_gray) #grafica
image_gray.save("D:/Vision/Taller 1/Punto3/imagen4.jpg") # guardamos la imagen D:\Vision\Taller 1\Punto3
plt.gray() #grafica
plt.axis("off") #para que no muestre los ejes del plano cartesiano 

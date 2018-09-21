#BASILIO SALDARRIAGA
#ANDERSON HERRERA

"""

PROBLEM 4: HISTOGRAM EQUALIZATION FOR COLOR IMAGE

Histogram equalization of color images require a transformation from RGB space to a new color space. For
example, we can use the YCbCr space, where Y represents the intensity. In this part of the homework, you
will implement the functions for histogram equalization of a rgb image.


a. Implement a function to transform an image from RGB to YCbCr space. The YCbCr space is defined
as:
    
Y = 0.299R + 0.587G + 0.114B
Cb = -0.169R – 0.331G +0.500B + 128
Cr = 0.500R – 0.419G – 0.081B + 128

Where R, G and B are the red, green and blue channel respectively.


b. Implement a function to transform an image from YCbCr to RGB space color. This transformation is
obtained by:
    
R = 1.000Y + 1.403(Cr - 128)
G = 1.000Y – 0.344(Cb - 128) – 0.714(Cr - 128)
B = 1.000Y + 1.773(Cb - 128)


c. Implement a function to perform the histogram equalization of a RGB image following the next steps:
Step 1: Transform the image from RGB to YCbCr
Step 2: Perform the histogram equalization to the Y channel
Step 3: Built a new image using the channel Y equalized, and the original Cb and Cr.
Step 4: Transform the new image from YCbCr to RGB
 

d. Use the function with a real RGB image. Plot the original image, the new RGB image, and both the
original and equalized histogram of Y.


"""

from PIL import Image #importacion de libreria
import numpy as np #importacion de libreria
import matplotlib.pyplot as plt #importacion de libreria
import sys #importacion de libreria
sys.path.append('/media/mariatorres/ADATA UFD/VAI92/Code/')


def YCBbCR(image): # Funcion  YCBbCR
    #Sprint(image)
    
    R = CANALES(image, 0)
    G = CANALES(image, 1)
    B = CANALES(image, 2)
    
    Y = 0.299*R + 0.587*G + 0.114*B
    Cb = -0.169*R - 0.331*G + 0.500*B + 128
    Cr = 0.500*R - 0.419*G - 0.081*B + 128
    yCBbCR = CANALES_unir(Y, Cb, Cr)
    return yCBbCR

def RGB(image): # funcion RGB
    R = 1.000*Y + 1.403*(Cr - 128)
    G = 1.000*Y - 0.344*(Cb - 128) - 0.714*(Cr - 128)
    B = 1.000*Y + 1.773*(Cb - 128)
    
def CANALES(im, canal): # funcion para recorrer los canales
    [row, col,c] = im.shape
    vec = np.zeros((row, col))
    
    for i in range(0, row-1):
        for j in range(0, col-1):
            vec[i,j] = im[i,j][canal]
    return vec

def CANALES_unir(c1, c2, c3):  # funcion para unir los canales
    [row, col] = c1.shape
    im = np.zeros((row, col, 3))
    im[:,:,0] = c1 
    im[:,:,1] = c2 
    im[:,:,2] = c3 
    #print(im)
    
    return im

def my_histograma(im): # funcion del hisotgrama
    [row, col] = im.shape
    vec = np.zeros(256)
    print(vec.shape)
    for i in range(0, row-1):
        for j in range(0, col-1):
            valor = im[i, j]
            vec[valor] = vec[valor] + 1
        return vec
 
    
def my_equal(im, h): # funcion de la ecualizacion
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

Im_g = Image.open('Penguins.jpg')
Im_ga = np.array(Im_g)
plt.imshow(Im_ga)
plt.show()

asd = YCBbCR(Im_ga)
print(asd) # imprime los valores convertidos de los canales
im2 = np.uint8(asd)
plt.imshow(im2)
plt.show()

Y = CANALES(asd, 0)
print(Y.astype(int))
h = my_histograma(Y.astype(int)) #realizacion del histograma pero con numeros enteros
plt.figure()
plt.bar(np.arange(256), h, color = 'purple' ) # muestra el histograma de color morado



# Falta equalizar 

"""
eq = my_equal(Y.astype(int)) # realizacion de la ecualiacion pero con numeros enteros
plt.figure()
plt.bar(np.arange(256), h)

#devido a que la imagen es muy nitida la ecualizacion lo que hace es dañar la image.

"""

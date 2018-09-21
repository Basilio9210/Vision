import numpy as np
 

    #este metodo recibe paramentros desde la función lineal, la imagen y el alor de Y 
    #y la tranforma con la función gamma
def my_gamma(image, gamma): #asi se declara una función en python 
    Im_ga = np.double(image)
    Im2 = Im_ga**gamma #acá ya queda la imagen en la funcion gamma
    Im2 = np.uint8(255*Im2/Im2.max())# se escala de double a uint8
    return Im2
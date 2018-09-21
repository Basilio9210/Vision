import numpy as np
 

    #este metodo recibe paramentros desde la función lineal, la imagen y el alor de Y 
    #y la tranforma con la función gamma
def my_gamma(image, gamma): #declaracion de la  una función my_gamma que recibe como parametro imagen y variable
    Im_ga = np.double(image) # transofrmacion de la imagen a DOUBLE
    Im2 = Im_ga**gamma #Imagen en la funcion gamma
    Im2 = np.uint8(255*Im2/Im2.max())#Escala de double a uint8
    return Im2
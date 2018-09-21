
"""
Punto 1 del taller 2

Integrantes:
    
    Basilio Saldarriaga
    Anderson Herrera
    
"""


from PIL  import Image
import numpy as np
import FuncionesFiltros as fun
import matplotlib.pyplot as plt
from scipy.ndimage import filters


""" Punto A """

Ig = Image.open('coins.jpg').convert('L')
Im_ga = np.array(Ig)
plt.gray()
plt.imshow(Ig)
plt.axis("off")
plt.title("imagen original en escala de grises")


""" Punto B """

[row, col] = Im_ga.shape
Im_n1 = np.double(Im_ga)
for i in range(0, row - 1):
    for j in range (0, col -1):
        Im_n1[i, j] = Im_n1[i, j] + np.random.uniform(0, 60)
 
plt.figure()
plt.imshow(Im_n1)
plt.axis("off")
plt.title("imagen con nivel de ruido (0, 60)")       
        
        
[row, col] = Im_ga.shape;
Im_n2 = np.double(Im_ga)
for i in range(0, row - 1):
    for j in range (0, col -1):
        Im_n2[i, j] = Im_n2[i, j] + np.random.uniform(0, 80)
                
plt.figure()
plt.imshow(Im_n2)
plt.axis("off")
plt.title("imagen con nivel de ruido (0, 80)")

        
[row, col] = Im_ga.shape;
Im_n3 = np.double(Im_ga)
for i in range(0, row - 1):
    for j in range (0, col -1):
        Im_n3[i, j] = Im_n3[i, j] + np.random.uniform(0, 100)
        
plt.figure()
plt.imshow(Im_n3)
plt.axis("off")
plt.title("imagen con nivel de ruido (0, 100)")        


 ##Punto C """

#FILTROS UNIFORMES

Im_f1 = filters.uniform_filter(Im_n1, 3)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 3x3 de la imagen 1")

Im_f1 = filters.uniform_filter(Im_n1, 5)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 5x5 de la imagen 1")

Im_f1 = filters.uniform_filter(Im_n1, 7)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 7x7 de la imagen 1")

Im_f1 = filters.uniform_filter(Im_n1, 9)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 9x9 de la imagen 1")




Im_f1 = filters.uniform_filter(Im_n2, 3)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 3x3 de la imagen 2")

Im_f1 = filters.uniform_filter(Im_n2, 5)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 5x5 de la imagen 2")

Im_f1 = filters.uniform_filter(Im_n2, 7)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 7x7 de la imagen 2")

Im_f1 = filters.uniform_filter(Im_n2, 9)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 9x9 de la imagen 2")



Im_f1 = filters.uniform_filter(Im_n3, 3)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 3x3 de la imagen 3")

Im_f1 = filters.uniform_filter(Im_n3, 5)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 5x5 de la imagen 3")

Im_f1 = filters.uniform_filter(Im_n3, 7)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 7x7 de la imagen 3")

Im_f1 = filters.uniform_filter(Im_n3, 9)
plt.figure()  
plt.gray()
plt.imshow(Im_f1)
plt.axis("off")
plt.title("filtro uniforme 9x9 de la imagen 3")


#FILTROS GAUSSIANOS


Im_f2 = filters.gaussian_filter(Im_n1, 0.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 1 con sigma igual a 0.5")

Im_f2 = filters.gaussian_filter(Im_n2, 0.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 2 con sigma igual a 0.5")

Im_f2 = filters.gaussian_filter(Im_n3, 0.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 3 con sigma igual a 0.5")

Im_f2 = filters.gaussian_filter(Im_n1, 0.7)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano  de la imagen 1 con sigma igual a 0.7")

Im_f2 = filters.gaussian_filter(Im_n2, 0.7)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 2 con sigma igual a 0.7")

Im_f2 = filters.gaussian_filter(Im_n3, 0.7)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 3 con sigma igual a 0.7")


Im_f2 = filters.gaussian_filter(Im_n1, 1)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 1 con sigma igual a 1")

Im_f2 = filters.gaussian_filter(Im_n2, 1)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 2 con sigma igual a 1")

Im_f2 = filters.gaussian_filter(Im_n3, 1)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 3  con sigma igual a 1")


Im_f2 = filters.gaussian_filter(Im_n1, 1.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 1 con sigma igual a 1.5")

Im_f2 = filters.gaussian_filter(Im_n2, 1.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 2 con sigma igual a 1.5")

Im_f2 = filters.gaussian_filter(Im_n3, 1.5)
plt.figure()  
plt.gray()
plt.imshow(Im_f2)
plt.axis("off")
plt.title("Filtro gaussiano de la imagen 3 con sigma igual a 1.5")



##""" Punto D"""

##FILTRO UNIFORME
print('')
print('FILTROS UNIFORMES')
print('')


#MSE PARA IMAGEN 1

Im_f1 = filters.uniform_filter(Im_n1, 3)
print ("Error cuadratico  para filtro uniforme 3x3 con ruido de 0,60 de la imagen 1  ")
print(str(fun.my_mse(Im_f1, Im_n1)))  
print('')      

Im_f1 = filters.uniform_filter(Im_n1, 5)
print ("Error cuadratico  para filtro uniforme 5x5 con ruido de 0,60 de la imagen 1  "  )
print(str(fun.my_mse(Im_f1, Im_n1)))        
print('')

Im_f1 = filters.uniform_filter(Im_n1, 7)
print ("Error cuadratico  para filtro uniforme 7x7 con ruido de 0,60 de la imagen 1  ")
print(str(fun.my_mse(Im_f1, Im_n1)))
print('')

Im_f1 = filters.uniform_filter(Im_n1, 9)
print ("Error cuadratico  para filtro uniforme 9x9 con ruido de 0,60 de la imagen 1  ")
print(str(fun.my_mse(Im_f1, Im_n1)))        
print('') 
 
   
#MSE PARA IMAGEN 2

Im_f1 = filters.uniform_filter(Im_n2, 3)
print ("Error cuadratico  para filtro uniforme 3x3 con ruido de 0,80 de la imagen 2  ")
print(str(fun.my_mse(Im_f1, Im_n2)))        
print('')

Im_f1 = filters.uniform_filter(Im_n2, 5)
print ("Error cuadratico  para filtro uniforme 5x5 con ruido de 0,80 de la imagen 2  ")
print(str(fun.my_mse(Im_f1, Im_n2)))        
print('')

Im_f1 = filters.uniform_filter(Im_n2, 7)
print ("Error cuadratico  para filtro uniforme 7x7 con ruido de 0,80 de la imagen 2 ")
print(str(fun.my_mse(Im_f1, Im_n2)))
print('')

Im_f1 = filters.uniform_filter(Im_n2, 9)
print ("Error cuadratico  para filtro uniforme 9x9 con ruido de 0,80 de la imagen 2  ")
print(str(fun.my_mse(Im_f1, Im_n2)))        
print('')


#MSE PARA IMAGEN 3

Im_f1 = filters.uniform_filter(Im_n3, 3)
print ("Error cuadratico  para filtro uniforme 3x3 con ruido de 0,100 de la imagen  ")
print(str(fun.my_mse(Im_f1, Im_n3)))        
print('')

Im_f1 = filters.uniform_filter(Im_n3, 5)
print ("Error cuadratico  para filtro uniforme 5x5 con ruido de 0,100 de la imagen 3 ")
print(str(fun.my_mse(Im_f1, Im_n3)))        
print('')

Im_f1 = filters.uniform_filter(Im_n3, 7)
print ("Error cuadratico  para filtro uniforme 7x7 con ruido de 0,100 de la imagen 3  ")
print(str(fun.my_mse(Im_f1, Im_n3)))
print('')

Im_f1 = filters.uniform_filter(Im_n3, 9)
print ("Error cuadratico  para filtro uniforme 9x9 con ruido de 0,100 de la imagen 3 ")
print(str(fun.my_mse(Im_f1, Im_n3)))        
print('')



##FILTRO GAUSSIANO

print('')
print('FILTROS GAUSSIANOS')
print('')


#MSE PARA IMAGEN 1
Im_f2 = filters.gaussian_filter(Im_n1, 0.5)
print ("Error cuadratico para filtro Gaussiano 0.5 de la imagen 1")
print(str(fun.my_mse(Im_f2, Im_n1)))  
print('')      

Im_f2 = filters.gaussian_filter(Im_n1, 0.7)
print ("Error cuadratico  para filtro Gaussiano 0.7 de la imagen 1")
print(str(fun.my_mse(Im_f2, Im_n1)))        
print('')

Im_f2 = filters.gaussian_filter(Im_n1, 1)
print ("Error cuadratico  para filtro  Gaussiano 1 de la imagen 1")
print(str(fun.my_mse(Im_f2, Im_n1)))
print('')

Im_f2 = filters.gaussian_filter(Im_n1, 1.5)
print ("Error cuadratico  para filtro Gaussiano 1.5 de la imagen 1")
print(str(fun.my_mse(Im_f2, Im_n1)))        
print('') 
    
#MSE PARA IMAGEN 2
Im_f2 = filters.gaussian_filter(Im_n2, 0.5)
print ("Error cuadratico para filtro Gaussiano 0.5 de la imagen 2")
print(str(fun.my_mse(Im_f2, Im_n2)))  
print('')      

Im_f2 = filters.gaussian_filter(Im_n2, 0.7)
print ("Error cuadratico  para filtro Gaussiano 0.7 de la imagen 2")
print(str(fun.my_mse(Im_f2, Im_n2)))        
print('')

Im_f2 = filters.gaussian_filter(Im_n2, 1)
print ("Error cuadratico  para filtro  Gaussiano 1 de la imagen 2")
print(str(fun.my_mse(Im_f2, Im_n2)))
print('')

Im_f2 = filters.gaussian_filter(Im_n2, 1.5)
print ("Error cuadratico  para filtro Gaussiano 1.5 de la imagen 2 ")
print(str(fun.my_mse(Im_f2, Im_n2)))        
print('') 


#MSE PARA IMAGEN 3

Im_f2 = filters.gaussian_filter(Im_n3, 0.5)
print ("Error cuadratico para filtro Gaussiano 0.5 de la imagen 3")
print(str(fun.my_mse(Im_f2, Im_n3)))  
print('')      

Im_f2 = filters.gaussian_filter(Im_n3, 0.7)
print ("Error cuadratico  para filtro Gaussiano 0.7 de la imagen 3")
print(str(fun.my_mse(Im_f2, Im_n3)))        
print('')

Im_f2 = filters.gaussian_filter(Im_n3, 1)
print ("Error cuadratico  para filtro  Gaussiano 1 de la imagen 3")
print(str(fun.my_mse(Im_f2, Im_n3)))
print('')

Im_f2 = filters.gaussian_filter(Im_n3, 1.5)
print ("Error cuadratico  para filtro Gaussiano 1.5 de la imagen 3")
print(str(fun.my_mse(Im_f2, Im_n3)))        
print('') 
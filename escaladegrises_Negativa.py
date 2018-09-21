from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

Im_g = Image.open('imagen_tres_quiz.jpg').convert('L')
Im_ga = np.array(Im_g) #crea la matriz 
print(Im_ga.shape) #tamaño de la matriz shape
Im1 = 255 - Im_ga #Invertir la image"""
plt.gray()
plt.imshow(Im_ga)
plt.axis("off") #para q no muestre el plano cartesiano 

plt.figure() #para q muestre las dos imagenes 
plt.gray()
plt.imshow(Im1)
plt.axis("off")
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:20:18 2018

@author: BASILIO.SALDARRIAGA
"""
import math
import numpy as np

def rgb_to_hsi(R, G, B):
    def get_H():
        if B < G:
            return get_c()
        else:
            return np.pi*2 - get_c()
 
    def get_S():
        if R+G+B == 0:
            return "undef"
        return 1-(3/(R+G+B))*min(R, G, B)
 
    def get_I():
        return (R+G+B)/3
 
    def get_c():
        return math.acos((2*R-G-B)/(2*math.sqrt((R-G)**2+(R-B)*(G-B))))
 
    return get_H(), get_S(), get_I()
 

#EJEMPLO
values = [(100, 0, 0), (0, 60, 0), (0, 0, 240), (122, 121, 122), (2, 243, 4)]
 
for pair in values:
    R, G, B = pair
    print("\n---------")
    print("R: {} | G: {} | B: {}".format(R, G, B))
    H, S, I = rgb_to_hsi(R, G, B)
 
    print("H: {0:.4f}".format(H))
    print("S: {0:.4f}".format(S))
    print("I: {0:.4f}".format(I))
    print("---------\n")



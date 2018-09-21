# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:57:31 2018

error cuadratico medio

@author: BASILIO.SALDARRIAGA
"""
import numpy as np

def my_mse(image1, image2):
    [n, l] = image1.shape
    n = n * l
    mse = sum(sum((image1 - image2)**2))/n
    return mse
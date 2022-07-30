import cv2 as cv
import numpy as np
from glob import glob
import os 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def croper(paths,cwd):
    for i,path in enumerate(paths):
        
        image = cv.imread(path)
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        r,c = gray.shape
        minimum = np.array([30]*c)
        

        
        
        for j in range(len(gray)):
            if list(gray[j] <= minimum).count(True) >= (c//3):
            
                gray = gray[j:]
                break

        
        
        
        cv.imwrite(f'processed_images/image{i}.png',gray)
    return glob(cwd + '/processed_images/*')


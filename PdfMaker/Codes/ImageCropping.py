import cv2 as cv
import numpy as np
from glob import glob
import os 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def croper(paths,cwd):
    for i,path in enumerate(paths):
        extension = path.strip().split('.')[-1]
        image = cv.imread(path)
        gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        
        
        gray = cv.resize(gray,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
        
        
        
        cv.imwrite(f'processed_images/image{i}.{extension}',gray)
    return glob(cwd + '/processed_images/*')


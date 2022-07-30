import cv2 as cv
import numpy as np
from glob import glob


def qualityoptimizer(paths,cwd):
    watermark = 'waterMaker/images.jpeg'
    waterMarkImage = cv.imread(watermark)

    for path in paths:
        image = cv.imread(path)
        arr = list(cv.split(image))
        # _,arr[0]  = cv.threshold(arr[0], 120, 255, cv.THRESH_BINARY)
        # _,arr[1]  = cv.threshold(arr[1], 120, 255, cv.THRESH_BINARY)
        # _,arr[2]  = cv.threshold(arr[2], 120, 255, cv.THRESH_BINARY)
        filtered_image = cv.merge(arr)
        r,c,d = filtered_image.shape
        # fourierTransformedImage = np.fft.fftshift(np.fft.fft2(img))
        # magnitude_spectrum = np.log(np.abs(fourierTransformedImage))
        # r,c = magnitude_spectrum.shape 
        # r1 = r//2
        # c1 = c//2
        # do = 300
        # hf = np.zeros((r,c))
        # for i in range(len(magnitude_spectrum)):
        #     for j in range(len(magnitude_spectrum[i])):
        #         if ((i - r1)**2 + (j -c1)**2)**0.5 >= do:
        #             hf[i,j] = 0
                    
        #         else:
        #             duv = ((i - r1)**2 + (j -c1)**2)
        #             hf[i,j] = np.exp(-duv/(2*do)**2)
        # final = fourierTransformedImage*hf
        
        waterMarkImage.resize((r,c,d))
        
        print(waterMarkImage.shape,filtered_image.shape)
        cv.imshow('water',waterMarkImage)
        cv.waitKey()
        # filtered_image = abs(np.fft.ifft2(final))
        
        # filtered_image -= waterMarkImage

       
        cv.imwrite(path,filtered_image)
    return glob(cwd + "/processed_images/*.png")
    
import cv2 as cv
import numpy as np
from glob import glob


def qualityoptimizer(paths,cwd):
    watermark = 'waterMaker/image.png'
    waterMarkImage = cv.imread(watermark)
    row,column,_ = waterMarkImage.shape
    for path in paths:
        image = cv.imread(path)
        img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(img, 100, 240, cv.THRESH_TOZERO)
        filtered_image = cv.merge([thresh,thresh,thresh])
        r,c,d = filtered_image.shape
        new_image_width = c
        new_image_height = r
        
        if row > r :
            waterMarkImage = waterMarkImage[:r,:,:]
        if column > c:
            waterMarkImage = waterMarkImage[:,:c,:]
        row,column,_ = waterMarkImage.shape
        color = (255,255,255)
        pad = np.full((new_image_height,new_image_width, 3), color, dtype=np.uint8)
        
        
        center_x = abs(r - row )//2
        center_y = abs(c - column)//2
        pad[center_x:center_x + row, center_y:center_y + column] = waterMarkImage
        
        gray_mark =  cv.cvtColor(pad, cv.COLOR_BGR2GRAY)
        mean = gray_mark.mean()
        ret, gray_mark = cv.threshold(gray_mark, 225, 255, cv.THRESH_BINARY_INV)
        gray_mark =gray_mark//15
        gray_mark = cv.merge([gray_mark,gray_mark,gray_mark])
        cv.imshow('water',gray_mark)
        cv.waitKey(0)
        filtered_image += gray_mark

       
        cv.imwrite(path,filtered_image)
    return glob(cwd + "/processed_images/*.png")
    
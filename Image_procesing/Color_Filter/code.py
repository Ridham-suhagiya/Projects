# Moduels Required 
import cv2 as cv
import numpy as np
import time


# Video File Path
file_path = "476-the-final-battle_QzqttURT.mkv"

# Reading the video
vid = cv.VideoCapture(file_path)
state = True



# timer after which you want the effect to take place
count = 1000
while state:
  
  if count > 0:
      count -=1
      
      state,imgd= vid.read()
      imgd_old = imgd.copy()
  else:
    state,imgd= vid.read()
    imgd_old = imgd.copy()



    b,g,r = cv.split(imgd)


    mx_pix = np.max(imgd,axis = 2)
    mx_pix = cv.merge([mx_pix,mx_pix,mx_pix])
    red = cv.merge([r,r,r])
    blue = cv.merge([b,b,b])
    green = cv.merge([g,g,g])
    imgd = np.where(red < blue,mx_pix,imgd)
    imgd = np.where(red < green , mx_pix,imgd)
  # Delay to make things synchronized  
  time.sleep(0.01)

  # Image displat (Color filtered)
  cv.imshow('Narutoo!!',imgd)
  

  if cv.waitKey(1) & 0xFF == ord('q'):
	      break


vid.release()
cv.destroyAllWindows()



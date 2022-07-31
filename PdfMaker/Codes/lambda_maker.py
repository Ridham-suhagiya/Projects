from glob import glob
import os 

import fpdf
from ImageCompression import pdfmaker  
from ImageCropping import croper
from qualityImprover import qualityoptimizer
# light karna hai 
# cropping 
# image 
def lambda_maker():
    cwd  = os.getcwd()
    
    
    paths = glob(cwd + "/images/*.png")      # paths to unprocessed images
    paths += glob(cwd + "/images/*.jpg")
    paths += glob(cwd + "/images/*.jpeg")
    
    
    paths = croper(paths,cwd)           # paths to processed images  (croped)    
    paths = qualityoptimizer(paths,cwd)     # Water Marking and image quality improvement
    
    
    pdf = fpdf.FPDF()

    pdfmaker(paths,pdf)          # Pdf making

lambda_maker()
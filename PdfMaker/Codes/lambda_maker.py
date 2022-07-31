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
    
    
    
    
    paths = croper(paths,cwd)           # paths to processed images  (croped)
    paths,dimensions = qualityoptimizer(paths,cwd)
    
    
    pdf = fpdf.FPDF()

    pdfmaker(paths,pdf,dimensions)

lambda_maker()
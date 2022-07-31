
def pdfmaker(paths,pdf,dimensions):
    
     
    for i in range(len(paths)):
        pdf.add_page()
        
        height,weidth = dimensions[i]       ## 1128, 800  -- > 210 , 290  
        height  = height//5.37
        weidth = weidth // 2.75


        pdf.image(paths[i],0,0,height,weidth)
    pdf.output("./test.pdf","F")
 
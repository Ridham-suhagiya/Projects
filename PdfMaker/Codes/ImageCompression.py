
def pdfmaker(paths,pdf):
    
    
    for path in paths:
        pdf.add_page()
        pdf.image(path,0,0,200,200)
    pdf.output("./test.pdf","F")

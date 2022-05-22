# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('/home/ralph/Dropbox/Biblioteca do calibre/Gojko Adzic/[Specification by Example_ How Successful Teams Deliver the Right Software] [By_ Adzic, Gojko] (46)/[Specification by Example_ How Successful - Gojko Adzic.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.getPage(110) 
    
# extracting text from page 
print(pageObj.extractText()) 
    
# closing the pdf file object 
pdfFileObj.close() 
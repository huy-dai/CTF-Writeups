# import parser object from tike
from tika import parser  
  
# opening pdf file
parsed_pdf = parser.from_file("scan.pdf")
  
print(parsed_pdf)
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['text']
  
# Printing of content 
print(data)
  
# <class 'str'>
print(type(data))
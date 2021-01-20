import re, os, PyPDF2
emails = []
#read file
#replace path with your directory
path = '/Users/antique/Documents/DIU email extractor/PDFs/'
print ('List of documents to process',os.listdir(path))
for file in os.listdir(path):
    if file.endswith(".pdf"):
        pdf_f = open(path+''+file, 'rb') 
        print('Now processing:', file)
        pdf_reader = PyPDF2.PdfFileReader(pdf_f)
        num_of_pages = pdf_reader.numPages
        for n in range(0, num_of_pages):
            page = pdf_reader.getPage(n) 
            s = page.extractText() #texts
            lst = re.findall(r'[a-z]+15-[0-9]+@diu.edu.bd', s) #email regex
            print('Email address found in this page:', len(lst))
            emails.extend(lst)
            print('Total so far :',len( all_email))
        pdf_f.close() 
#print(emails)
#save to text file
import pandas as pd    
df = pd.DataFrame(emails)
#csv_data = df.to_csv(index=False, header=False)
df.to_csv('emails.csv', index=False, header=False)
print('Saevd to file')

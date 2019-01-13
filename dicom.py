import pydicom as pd


filename1 = open("/home/arnab/Downloads/ttfm.dcm",'rb')                      #reading the file in read-binary mode
ds1 = pd.filereader.dcmread(filename1,force=True)                            #force Set to True to force reading even if no File Meta Information header is found
filename2 = open("/home/arnab/Downloads/bmode.dcm",'rb')
ds2 = pd.filereader.dcmread(filename2,force=True)


file = open("/home/arnab/Downloads/output.txt",'w',encoding="utf-8")          #opening the output file .txt

file.write("The DICOM Tags in ttfm.dcm file : \n\n ")

n = [[],[]]

element1 = ds1.elements()
element2 = ds2.elements()

for elem,k in zip(element1,range(0,57)):
    n = elem.tag
    file.write(str(k+1)+". "+str(n)+" "+ds1.dir()[k]+"\n")
    
file.write("\n\n\nThe DICOM Tags in bmode.dcm file : \n\n")

for elem,k in zip(element2,range(0,57)):
    n=elem.tag
    file.write(str(k+1)+". "+str(n)+" "+ds2.dir()[k]+"\n")
    
file.close()                                                                   #closing all files
filename1.close()
filename2.close()
    
    

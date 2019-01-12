import pydicom as pd

filename1 = open("ttfm.dcm",'rb')                      #reading the file in read-binary mode
ds1 = pd.filereader.dcmread(filename1,force=True)      #force Set to True to force reading even if no File Meta Information header is found
filename2 = open("bmode.dcm",'rb')
ds2 = pd.filereader.dcmread(filename2,force=True)

ds1.dir()                                             #display DICOM Tags of ttfm.dcm file
print("\n")
ds2.dir()                                             #display DICOM Tags of bmode.dcm file


#Writing the output in a .txt file
file = open("output.txt",'w')
file.write("The DICOM Tags in ttfm.dcm file : \n ")
file.write("{}".format(ds1.dir()))
file.write("\nThe DICOM Tags of bmode.dcm file : \n")
file.write("{}".format(ds2.dir()))

filename1.close()
filename2.close()
file.close()

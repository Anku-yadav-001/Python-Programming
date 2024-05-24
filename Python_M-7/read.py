#Python can be used to perform operations on files.

f= open("Python_M-7/demo.txt" ,"r") #open the file
data=f.read() #print while file data
data1=f.readline() #read a one line at a time
data2=f.readlines() #read file data in the form of array
data3=f.readline(3) #print only 3 char's
print(data)
f.close() #close the file
f=open("Python_M-7/demo.txt","a")
f.write("This is new file")  #w mode overwrite the file
f.write("\nWe were add some data like addresss information") #a mode append the data at the end
f.close()

#r+ - if we want to overwrite the file from starting than we can use it
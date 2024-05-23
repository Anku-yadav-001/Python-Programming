#Tuple-It is also a built-in data type in python
#immutable
#indexing allowed
#()
#like as string

tuple=() #empty tuple
tuple1=(1,2,3,4,3,5,7,8)
# tuple1[0]=20 #error
print(len(tuple1))

#if only one element in tuple then we have to mention , at the last of element otherwise it will consider as a integer value in python 
tuple2=(1) #consider integer
tuple3=(1,) #consider tuple

#SLICING
tuple4=(3,4,5,3,5,3,5)
print(tuple4[2:5]) #(5, 3, 5) 

#Index
print(tuple4.index(5)) #print the first index of the given element

#count
print(tuple4.count(5)) #count the number of occurence of element
#List-List is a built in data type in python which is used to store the values

#lists are mutable(changable) 
#indexing allowed
#[]
#like as array

marks=[23,43,65,77,99,66,66]
print(marks) #[23,43,65,77,99,66,66]
print(marks[0]) #23

details=["aman",19,"narmadapuram"]
print("Name: ",details[0]) #aman
print("Age: ",details[1])  #19
print("Address: ",details[2]) #Narmadapuram

#SLICING
print(marks[2:6]) #[65, 77, 99, 66]

#LIST METHODS
lists=[5,3,2,6,8,4,5]

lists.append(1) #add element at last
lists.sort() #sort the list in ascending order
lists.sort(reverse=True) #sort the list in descending order
lists.remove(6) #remove the first occurance given element
lists.insert(2,10) #add element on given index
lists.reverse() #reverse the string
lists.pop() #delete the last element from a list
lists.pop(4) #delete the element in given index
print("Copy ",lists.copy()) #create a copy of list
print(lists)

emptyList=[] #empty list
print(emptyList) 
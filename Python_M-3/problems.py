#WAP to ask the user to there name of 3 favorite movies and store it into list

movie1=input("Enter first movie: ")
movie2=input("Enter second movie: ")
movie3=input("Enter third movie: ")

list=[]
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)

#WAP to check the list contain palindrom elements or not

list1=[1,2,3,2,1]
list2=list1.copy() #copy the list1 in list2
list2.reverse()  #reverse the list2
if(list1==list2): #if the list1 and list2 are queal then 
    print("Yes list is palindrom")
else:
    print("List is not palindrom")

# WAP to count number of students with grade A in a tuple
tuple=("B","C","D","F","A","A","B","A")
tuple1=tuple.count("A")
print(tuple1)

# WAP to shor the given list form "A" to "D"
lists=["B","C","D","F","A","A","B","A"]
lists.sort()
print(lists)

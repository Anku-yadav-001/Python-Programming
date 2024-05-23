#Sets-it is also a dtata structure in python

#it store unique values
#set-mutable-we can add-or-delete the elements of set but can not update the value in set
#set-elements-immutable
#unordered
#{}
#we can not store list and dictionary in set

sets={1,2,3,4,5,6,"Hello","aman"}
print(sets) #{1, 2, 3, 4, 5, 6, 'Hello', 'aman'}
print(type(sets)) #set
print(len(sets)) #8

#if we add duplicate values in set it will not throw any error, it just ignore them
set1={1, 4, 4,3,3,3,6,5,7,8,9,"hello","hello"}
print(set1) #{1, 3, 4, 5, 6, 7, 8, 9, 'hello'}

#if we write empty set so we can write like this set()
empty_set={} #consider empty dictionary
print(type(empty_set)) #dictionary
empty_set1=set() #consider empty set
print(type(empty_set1)) #set

#MATHODS
#1. add()-add element
our_set=set()
our_set.add(1)
our_set.add(2)
our_set.add(2)
our_set.add("aman")
our_set.add(3)

#2. remove()-delete the given element
our_set.remove(2) 

#3. pop()-remove a random value
our_set.pop()

#4. clear()-clear the set(empty)
our_set.clear()
print(our_set) 

#5. union-comnine 2 sets and combine only unique value
a={1,2,3,3,4}
b={3,4,5,6}
c=a.union(b) 
d=a.intersection(b)
print(c) #{1, 2, 3, 4, 5, 6}
print(d) #{3, 4}
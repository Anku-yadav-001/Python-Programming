# Store following word meanings in a python dictionary :
#     table : “a piece of furniture”,“list of facts & figures”
#     cat : “a small animal”

dict={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(dict)


# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#     ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

students={'python','java','C++','python','javascript','java','python','java','C++','C'}
print(len(students))#5


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
math=input("Enter maths number: ")
physics=input("Enter physics marks: ")
chemisty=input("Enter chemistry marks: ")
new_dict={}
new_dict.update({"maths":math})
new_dict.update({"physics":physics})
new_dict.update({"chemistry":chemisty})
print(new_dict)


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

#method-1
set1={
    9,"9.0" 
}

#method-2
sets={ 
    ("int",9),
    ("float",9.0)
}
print(sets)
#Constructor-All class have constructor function classed __init__, which is always executed when the object has been initiated

#python automatically create constructor

class Student:
    college_name="ABC college" #class attribute
    #default constructor
    def __init__(self):
        pass
    
    #parametrized constructor
    def __init__(self,fullname,age):
        self.name=fullname #object attribute
        self.age=age
        print("constructor working...")
    def say_hello(self):
        print("Hello dear, ",self.name)
        return
        
std1=Student("Aman",19)
print(std1.name,std1.age) #aman 19
std2=Student("Anku",20)
print(std2.name,std2.age) #anku 20
print(Student.college_name) #ABC college

#object attribute>class attribute 

print(std1.say_hello()) #Hello dear,  Aman
print(std2.say_hello()) #Hello dear,  Anku
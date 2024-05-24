#Inheritance- when one class inherit the properties of another class it is know as inheritance.

#base class/parent class
#       ^
#       |
#       |
#child class/derived class

class Car:
    @staticmethod
    def start():
        print("car started...")
        
    @staticmethod
    def stop():
        print("car stoped...")
        
class Toyota(Car):
    def __init__(self,name):
        self.name=name
        
c1=Toyota("fortuner")
c1.start()
c1.stop()

#there are 3 types of inheritance
#1. single level(above example is a example of single inheritance)
#2. multilevel 
#3. multiple

#2. multi level inheritance
class College:
    def __init__(self):
        pass
    def college_print(self):
        print("You belong to this class")
    
class Department(College):
    def __init__(self):
        pass
    def deparment_print(self):
        print(" and this depratment")
        
class Student(Department):
    def student_name(self):
        print("you are the student of CSE")
        

s1=Student()
s1.student_name()
s1.deparment_print()
s1.college_print()


#3. Multiple inheritance
class A:
    dataA="hello aman this is class A"
    
class B:
    dataB="hello aman this is class B"
    
class C(A,B):
    dataC="hello aman this is class C"
    
c=C()
print(c.dataC)
print(c.dataB)
print(c.dataA)


#super-it is a keyword which is used to access the method/data members of parent class

class State:
    def __init__(self,name):
        self.name=name
        
    def state_greet(self):
        print("our lovely MP")
        
class District(State):
    def __init__(self,s_name,name):
        self.s_name=s_name
        super().__init__(name)
        super().state_greet()

obj1=District("narmadapuram","madhya pradesh")
print(obj1.s_name) #narmadapuram
print(obj1.name) #madhyapradesh
obj1.state_greet()
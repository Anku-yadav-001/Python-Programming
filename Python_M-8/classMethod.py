#Class method-a class method bound to a class & receive the class as explicit first args

# @classmethod-decorator
class Student:
    name="anonymous"
    # def changename(self,name):
    #     # self.name=name #change only obj data member value
    #     self.__class__.name=name #change class member value
    #     Student.name=name #chnage class mebmer value
    @classmethod    
    def changename(cls,name):
         cls.name=name
     

s1=Student()
s1.changename("raghav")
# print(s1.name)
# print(Student.name)


# self.__class__.name=name
# Person.name=name 
# @classmethod


#property-if we want to use method as a property then we can use property decorator
# @property-decorator
class Marks:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property 
    def percentage(self):
             return (self.phy+self.chem+self.math)/3
m1=Marks(40,50,80)
print(m1.percentage)
m1.chem=100
print(m1.chem)
print(m1.percentage)
        

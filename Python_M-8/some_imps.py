#del -del keyword is used to delete the object properties or object itself.

class Student:
    def __init__(self,name):
        self.name=name
    
s1=Student("aman")
del s1 #object deleted


#Private attributes-means the members are functions are accessable only inside the class

class Account:
    def __init__(self,acc_name,acc_password):
        self.acc_name=acc_name
        self.__acc_password=acc_password #private member
        
    
    def __print_account(self): #private method
        print("bank details:",self.acc_name)
        
    #if we want to access the pricate methods so-
    def details(self):
        self.__print_account()
        
a1=Account("SBI","2345678")
print(a1.acc_name) #public member(by default)
# print(a1.acc_password) #private member
# print(a1.print_account()) #private method
print(a1.details())


print("name {name} and age {age}".format(name="aman", age=23))
nick="anku"
year=2025
print("name %s and year %d"%(nick,year))

a=40
b=20
assert a>b,"yes"

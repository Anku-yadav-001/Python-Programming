#Encapsulation- wrappping the data and function in a single unit(object).

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def print_average(self):
        sum=0
        for num in self.marks:
            sum=sum+num
        print("hi",self.name,"you got",sum/3,"marks")
        return

s1=Student("aman",[20,20,20])
s1.print_average()
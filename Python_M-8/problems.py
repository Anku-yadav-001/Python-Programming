# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

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
        
        
#Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    def debit(self,n):
        self.balance-=n
        print(n, "rupee deducted")
    
    def cradit(self,n):
        self.balance+=n
        print(n,"rupee credit")
    
    def print_balance(self):
        print("Total balance:",self.balance) 
    
acc1=Account(1000,"123aman")
acc1.debit(200)
acc1.cradit(100)
acc1.print_balance()
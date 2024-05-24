#Static method- that don't uses self parameter

#class level method is called as atatic methods
# @staticmethod-decorator

class Car:
    @staticmethod #decorator -static method(take a function as input and change the behaviour of the function and return the function)
    def greeting():
        print("hello guys!")
        
c1=Car()
c1.greeting()
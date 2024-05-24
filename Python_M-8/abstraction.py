#Abstraction- Hinding the unnecessary/implementation details and only show the relavent information to users.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start_car(self):
        self.acc=True
        self.clutch=True
        print("Car started...")
    
c1=Car()
c1.start_car() 
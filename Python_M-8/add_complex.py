
class Complex:
    def __init__(self,real,img): #__init__ dunder function
        self.real=real
        self.img=img
    
    def show(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,n): #__add__ dunder function
        realA=self.real+n.real
        imgA=self.img+n.img
        return Complex(realA,imgA)
    
    def __sub__(self,n): #__sub__ dunder function
        realA=self.real-n.real
        imgA=self.img-n.img
        return Complex(realA,imgA)
    
    
c1=Complex(4,5)
c2=Complex(2,3)
c1.show()
c2.show()
c3=c1+c2
c3.show()
c4=c1-c2
c4.show()
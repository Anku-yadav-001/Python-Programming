#input is function in python which is used to take the input form user-keyboard

input("Enter your name: ") #Enter your name
#by defult the value of input is str

#we can change the type of our input using int() float() bool() etc
int(input("Enter your age"))
float(input("Enter your marks"))
bool(input("Are you studying?"))

# let's take the information of a user

name=input("Enter your name: ")
age=int(input("Enter your age: "))
cgpa=float(input("Enter your marks: "))
studying=bool(input("Are you studying?: "))

print("----------USER INFORMATION---------")
print("Name: ",name)
print("Age: ",age)
print("CGPA: ",cgpa)
print("Studying: ",studying)

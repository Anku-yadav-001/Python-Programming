#_if__elif__else_ =used to perform conditional operations

#if-else
mobile=7898446814
if(mobile==7898446814): #if condition is true then it will enter in this block, otherwise else
    print("Yes this is aman's mobile numer")
else:
    print("No this another person mobile number")
    
age=19
if(age>=18):
    print("You can vote now!")
else:
    print("You can not vote")
 
 
#elif
name="aman"
if(name=="anku"):
    print("Your name is anku")
elif(name=="aman"):
    print("Your name is aman") 
else:
    print("You have no name assigned till now!")  
    
#nested if else
age1=20
if(age1>18): #if age1 is grater than 18
    if(age1==20):
        print("Your age is 20") #if age1 is equal to 20
    else:
        print("Not now!") #if age1 is not equal to 20
else:
    print("Please enter another age") #if age1 is not greater than 18


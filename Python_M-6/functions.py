#FUNCTION- it is a block of code which is used to perform specific tasks.
# to reduce redundency

#to define the function- def fun_name(parm1,parm2):

def calculate_sum(a,b): #function declaration
    print(a+b)
    
calculate_sum(5,10) # 15-function call

def calculate_multiplication(a,b):
    return a*b

ans=(calculate_multiplication(4,2))
print(ans)

# convert USD to INR(1$=83rs)

def convert_money(usd_value):
    inr_value=usd_value*83
    print(usd_value,"USD = ",inr_value,"INR")
    
convert_money(2) #2 USD =  166 INR
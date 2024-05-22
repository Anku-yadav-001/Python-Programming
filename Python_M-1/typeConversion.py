# There are 2 techniques to convert the type of variable
# 1. type conversion(automatically)
# 2. type casting

#1. type conversion
#python authmatically convert the ty[e of variables of we not mention explicitly
a=10
b=10.5
print(a+b) #20.5- python automatically convert the int to float because the priority of flocat is high

#2. type casting
#we have to manually mention the type of variable
c=20
d=4.5
e="2" #string
#if we want to change the type of d from float to int then
print(c+int(d)) #24
print(c+int(e)) #22 

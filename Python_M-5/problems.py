# Print numbers from 1 to 100 using while loop
i=1
while i<=100:
    print(i)
    i+=1

# Print numbers form 100 to 1 using while loop
j=100
while j>=1:
    print(j)
    j-=1
    
# Print multiplication table of a number n
n=int(input("Enter a number: "))
k=1
while k<=10:
    print(n," * ",k," = ",n*k)
    k+=1

# Print the elements of the following list using a loop:
list= [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
iterator=0
while iterator<=len(list)-1:
    print(list[iterator])
    iterator+=1
    
# Search for a number x in this tuple using loop:
tuple=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=25
y=0
while y<=len(tuple)-1:
    if(tuple[y]==x):
        print("Element fount at: ",y," position")
    y+=1

# Print the elements of the following list using a loop:
items=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in items:
    print(i)

# Search for a number x in this tuple using loop:
data=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x=36
for i in data:
    if(i==x):
        print("Element found")
        break
else:
    print("nahi mila")

# WAP to find the sum of first n numbers. (using while)
n=5
sum=0
i=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

# WAP to find the factorial of first n numbers. (using for)
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial is: ",fact)
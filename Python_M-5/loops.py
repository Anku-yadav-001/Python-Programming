#LOOPS-Used to repeat the instructions

#1. while loop
#2. for loop

#1. WHILE LOOP
count=5 #iterator
while count>=1: #condition
    print(count) #work
    count-=1 #change iterator

#BREAK AND CONTINUE
#Break-it is used to break the loop when the given condition will encounter
i=1
while i<=5:
    if(i==4):
        break
    print(i)
    i+=1
#it will print 1,2,3 after than the conditon i==4 encounter so then loop is terminate

#Continue-it is used when we want to skip the something in a loop
j=1
while j<=5:
    if(j==4):
        j+=1
        continue
    print(j)
    j+=1
#it will print 1,2,3,5 not 4 because if j==4 it just increase the value of j not print because of continue

# FOR LOOP
#used for sequential traveral
lists=[2,4,3,5,4,5,6,7]
for i in lists:
    print(i)

tuples=(4,3,5,4,6,7,6,7,6)
for j in tuples:
    print(j)

names=["aman","anku","shiv","raghav"]
for n in names:
    print(n)

address="namradapuram"
for k in address:
    print(k)
else:
    print("End of loop")

# RANGE
#It return sequance of numbers
#start value 0 by default and increase by 1 by default
#used with for loop

#range(start,stop,step)
for i in range(10):#(stop)
    print(i) #0,1,2,3,4,5,6,7,8,9
    
for j in range(1,11):#(start,stop)
    print(j) #1,2,3,4,5,6,7,8,9,10
    
for k in range(1,10,2):#(start,stop,step)
    print(k) #1,3,5,7,9
    

#PASS
#it is used when we dont want to print anything in loop, if we not mention anything in loop it will throw an error
for z in range(1,5):
    pass
print("Some useful work")
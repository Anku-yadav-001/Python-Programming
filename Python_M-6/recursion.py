# RECURSION- function call itself is known as recursion

#declare function
#base case
#work
#call itself

def print_number(n):
    if(n==0):
       return
    print(n)
    print_number(n-1)
    
print_number(10) #10,9,8,7,6,5,4,3,2,1


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
result=factorial(5)
print(result)

def calcualte_sum(n):
    if(n==0):
        return 0
    return calcualte_sum(n-1)+n
    
answer=calcualte_sum(5)
print(answer)

def print_list(list,ind):
    if(ind==len(list)):
        return 
    print(list[ind])
    print_list(list,ind+1)

data=["aman","anku","ram","raghav"] 
print_list(data,0)
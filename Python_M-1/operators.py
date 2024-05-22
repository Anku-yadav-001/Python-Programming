# Operators are the special symbols that is used to perform some operations

# Arithmatic operator
# _+__-__*__/__%__**_
a=20
b=10
print(a+b) #addition-30
print(a-b) #subtraction-10
print(a*b) #multiplication-200
print(a/b) #division-2
print(a%b) #modulo-0
print(a**b) #power-10240000000000

#Relational/comparasion operators
# _==__!=__>__<__<=__>=_

print(a==b) #False
print(a!=b) #True
print(a>b) #True
print(a<b) #False
print(a<=b) #False
print(a>=b) #True

#Assignment Operator
# _=__+=__-+__*=__/=__%=__**=_
a=b
print(a) #10
a+=b
print(a) #20
a-=b
print(a) #10
a*=b
print(a) #100
a/=b
print(a) #10
a%=b
print(a) #0.0
a**=b
print(a) #0.0

#Logical Operators
#_not__or__and_
c=10
d=20
e=True
print(not e) #False
print(c==10 or d==0) #True-any of the condition is true then it will return true otherwise false
print(c==10 and d==20) #True-both conditions are true then it will return true otherwise false

#String-it is a collection of characters

#we can write string's in 3 ways that is
# 'aman'
# "aman"
# """"aman"""

str1="Hello i am aman, and i am form narmadapuram"
print(str1)
# if we want to print `Hello i am aman` in one line and rest of string in second line so we can use excape characters in python
print("Hello i am aman,\nand i'm from narmadapuram")

#Operations on string
#1. concationation-addition of 2 or more strings
str2="aman"
str3="yadav"
print(str2+" "+str3) #aman yadav

#2.  #len()-used to calculate the length of string
print(len(str2)) #4
print(len(str3)) #5

#3. slice-used to access some part of string(it takes starting and ending index)
str4="aman-yadav"
print(str4[slice(1,4)]) #man(positive indexing)
print(str4[slice(5,len(str4))]) #yadav(positive indexing)
print(str4[slice(-5,-1)]) #yada(negative indexing)

#4. endsWith()-if the string ends with give string then it will return true
str5="Hello i am a coder"
print(str5.endswith("er")) #True
print(str5.endswith("e")) #False

#5. capitalize()-it will change our string first latter capital
str6="hello i am a coder"
print(str6.capitalize()) #Hello i am a coder

#6. replace()-it will replace given old value to new value 
print(str6.replace("coder","cricketer")) #Hello i am a cricketer

#7. find()-it find out the given value if the value exist it will return its index
print(str6.find("coder")) #13

#8. count()-it count the occurance of a latter/word
print(str6.count("a")) #2
print(str6.count("hello")) #1
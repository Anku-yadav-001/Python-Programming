#doc_string-it is a decription about the code, and we can write doc string just above the code

#it is declare by using """code description"""

#docstring VS comments
#docstring is a executale part of the program, but commments is not executable part of our code.

#we can access the docstring by using __doc__

def sum(a,b):
    '''
    this function takes 2 arguments a and b and return the sum of these 2 arguments 
    '''
    return a+b

print(sum(2,4)) #6
print(sum.__doc__) #this function takes 2 arguments a and b and return the sum of these 2 arguments 

#PEP 8- python enhancement propoosal
#it is a document which provide guidelines and best practice for how to write python code

import this 
#correct answer- it prints "Zen of Python"
#it will provide all the document related to our code
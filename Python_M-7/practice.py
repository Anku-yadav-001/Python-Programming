# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using python.
# I like programming in python
with open("Python_M-7\practice.txt","w+") as f:
    f.write("Hi evenyone\nwe are learning File I/O\nusing Python\nI like programming in python")
    data=f.read()
    print(data)

# WAF that replace all occurrences of “java” with “python” in above file.
with open("Python_M-7\practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Python","Javascript")

with open("Python_M-7\practice.txt","w") as f:
    f.write(new_data)

# Search if the word “learning” exists in the file or not.
with open("Python_M-7\practice.txt","r") as f:
    data=f.read()
    word="learning"
    if(data.find(word) !=-1):
        print("Found")
    else:
        print("not found")

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.
def check_char_line():
    word="learning"
    data=True
    line=1
    with open("Python_M-7\practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line+=1
    return -1

check_char_line()

# From a file containing numbers separated by comma, print the count of even numbers.
#method-1
with open("Python_M-7\practice.txt","r") as f:
    data=f.read()
    num=""
    count=0
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            if(int(num)%2==0):
                count+=1
                print("Count of even:", count)
            num=""
        else:
            num+=data[i]

#methos-2
with open("Python_M-7\practice.txt","r") as f:
    data=f.read()
    nums=""
    count=0
    lists=data.split(",")
    for i in lists:
        if(int(i)%2==0):
            count+=1
    print(count)       
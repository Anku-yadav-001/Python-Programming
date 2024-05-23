#Dictionary is a datastructure which is used to store the value in key value-pairs

#mutable
#{}
#key should be unique
#unordered
#we can make key-string,int,tuple,float but not list

#empty dectionary
dictionary={}
# "key":"value"
dict={
    "name":"aman",
     "age":19,
     "single":True,
     "skills":["javascript","java","python","react","c","c++"],
     "hobbies":("cricket","gardening","coding","tavelling"),
      "address":"narmadapuram",
      461661:"pin code"
}
print(dict) #whole dict
print(type(dict)) #dict

# we can access the value form an object by using keys
print(dict["name"]) #aman
print(dict["age"]) #19
print(dict["single"]) #True
print(dict["skills"]) #['javascript', 'java', 'python', 'react', 'c', 'c++']
print(dict["hobbies"]) #('cricket', 'gardening', 'coding', 'tavelling')
print(dict["address"]) #narmadapuram
print(dict[461661]) #pin code

print(type(dict["hobbies"])) #tuple
dict["name"]="anku"
print(dict["name"]) #anku

#NEASTED DICTIONARY
dict1={
    "name":"aman",
    "age":19,
    "is_adult":True,
     "address":{
         "state":"MP",
          "city":"narmadapuram",
           "fix-address":{
                "village":"managaon",
                "home":45,
                 "location":"near talab managaon"  
           }
     }
}
print(dict1["name"]) #aman
print(dict1["address"]["city"]) #narmadapuram
print(dict1["address"]["fix-address"]["village"]) #managaon
print(dict1["address"]["fix-address"]["location"]) #near talab managaon

#1. keys()-return all the keys
print(dict1.keys()) #['name', 'age', 'is_adult', 'address']

#2. values()-retunr all the values
print(dict1.values()) 

#3. items()-return all the ley value as tuple
print(dict1.items()) 

#4. get()-return the value of key that is given as args
print(dict1.get("name"))

#5. update()-add the new key-value pair
updated=dict1.update({"studying":True})

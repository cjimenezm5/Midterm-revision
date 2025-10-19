#tupples are similar to lists but they are immutable, yiou can't change the values
# [] = list, () = tupples


tup = (21, 36, 14, 25)

print(tup)

tup[1] = 33 #try to change the second element but CAN'T

tup.index(21) #tells you where the element is
 
#sets are a collection of unique elements. {} = sets

set = {22,24,14,21,5}

print(set)  #when printing the set, the order changes using hashes (to access the elements as quick as posisble)

#indexes are NOT supported in sets, but you CAN change the values

#DICTIONARIES 

data = {1: "Carmen", 2: "María", 3: "Alba"}

data[1] #prints out Carmen, if put 4, gives error

data.get(1) #also prints out Carmen, if use 4, doesn't output anyhtin

print(data.get(4)) # with 4, it prints out None

keys = ["Carmen", "María", "Alba"]
values = ["Python", "Java", "JS"]

#now merge these 2 into 1:

dat2 = dict(zip(keys, values))

print(dat2)

dat2["Carmen"] #gives the value for that key

dat2["Monica"] = "CS" #adds value
print(dat2)

del dat2["María"] #deletes values
print(dat2)


#create a new dictionary which will have lists and dictionaries inside

prog = {"JS": "Atom", "CS": "VS", "Python": ["Pycharm", "Sublime"], "Java" : {"JSE":"Netbeans", "Hola" : "Adiós" }}

prog["JS"]
prog["Python"]
prog["Python"][1] #select second element in list
prog["Java"]
prog["Java"]["Hola"]
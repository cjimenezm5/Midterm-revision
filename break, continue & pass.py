
x = int(input("How many candies do you want?"))
av = 5

i = 1

while i<=x:

    if i> av:
        break

    print ("Candy")
    i += 1


print("bye") 



#print numbers from 1-100 except those divisibel by 3 or 5

for i in range(0,100):

    if i%3 == 0:
        continue    #will skip before the execution (doesn't jump out of the loop)
    
    elif i%5 ==0:
        continue

    print (i)




#print only even numbers

for i in range(0,100):

    if i%2 != 0:
        pass
    else:
        print(i)





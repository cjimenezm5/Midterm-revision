

# for and else together


nums = [12,15,18,21,26]

#check if the list is divisible by 5


for i in nums:
    if i%5 ==0:
        print(i)


nums_2 = [10,15,18,21,26]

#check if the list is divisible by 5


for i in nums_2:
    if i%5 ==0:
        print(i)    #this will print both 10 and 15



for i in nums_2:
    if i%5 ==0:
        print(i)
        break   #this will stop at the FIRST number that is divisible by 5



nums_3 = [11,17,18,21,26]


for i in nums_3:
    if i%5 ==0:
        print(i)
        break
else:
    print("not found")  #indented at the same level as for



























#Get data input

with open(r'''C:\Users\ryan.hayes\Downloads\Code\AdventofCode\Day1\day1.in''') as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)

#Traverse every String in our Data
max = 0
max2 = 0 #Elf with second highest calories
max3 = 0 #Elf with third highest calories
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count
    

print("Max: ", max)
print("Max2: ", max2)
print("Max3: ", max3)
print("Answer to part 2: ", max+max2+max3)
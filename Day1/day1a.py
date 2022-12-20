#Get data input

with open(r'''C:\Users\ryan.hayes\Downloads\Code\AdventofCode\Day1\day1.in''') as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

#Traverse every String in our Data
max = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count

print("Count= ", count)
print("Max=", max)
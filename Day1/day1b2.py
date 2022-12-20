elves = []
calories = []
elf = []

with open(r'''C:\Users\ryan.hayes\Downloads\Code\AdventofCode\Day1\day1.in''') as file:
    for line in file:
        data = [line.strip() for line in file]

    for item in data:
        if item != "":
            elf.append(int(item))
        if item == "":
            elves.append(elf)
            elf = []

for elf in elves:
    elf_cal = sum(elf)
    calories.append(elf_cal)

#print(data)

calories.sort()
#print(calories)
print("")
top_3 = calories[-1] + calories[-2] + calories[-3]
print("Answer to Part 2: ", top_3)
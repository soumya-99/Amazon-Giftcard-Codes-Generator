import random

def randomize(choice):
    data: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    result: str = ""
    while choice >= 1:
        c = random.choice(data)
        result = result + c
        choice = choice - 1
    return result
    
number = input("Number of codes you want?\n> ")
print("")
n = int(number)

for i in range(n):
    print(randomize(4)+"-"+randomize(6)+"-"+randomize(5))

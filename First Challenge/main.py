import random as r

# User input on random names
randomStr = input("Should Names be generated randomly? (y/n): ")

# Ternary operator, instead of three line if else statement
random = True if randomStr == "y" else False
randomList = []

# Overengineered part to ease the testing I guess?
if random:
    randomNames = ["Nazih", "Spounka", "Aymen", "Ahmed",
                   "Zaim", "Someone", "Zack", "Zex", "Vladimir", "George", "John", "Vadim"]
    randomList = [x for x in randomNames if r.randint(0, 100) % 3 == 0]
    print(randomList)
else:
    randomLength = int(input("Enter number of names: "))

    while(randomLength > 0):
        randomList.append(input("Enter Name: "))
        randomLength -= 1

# This line is easier than it looks
# It simply splits the name / string then puts it back together, this is to avoid counting whitespaces
result = [len("".join(x.split())) for x in randomList]
print(result)

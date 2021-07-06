import random

rolling = True

while rolling:
    print(random.randint(1,6))
    again=input("Do you want to print again: (y\n) ")
    if again.lower() == "y":
        continue
    else:
        break
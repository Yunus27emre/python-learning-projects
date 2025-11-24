import random

heads=0
tails=0

money_surface=["heads","tails"]

throw_money=int(input("How much money throw? "))

while throw_money>0:
    surface=random.choice(money_surface)
    if surface=="heads":
        heads+=1
        print("Came up heads")
    else:
        tails+=1
        print("Came up tails")
    throw_money-=1

print(heads,"heads")
print(tails,"tails")
while True:
    number=int(input("Enter positive a number :"))
    if number>0:
        break

factoriel=1
for x in range(1,number+1):
    factoriel*=x

print("{}! = ".format(number)+str(factoriel))
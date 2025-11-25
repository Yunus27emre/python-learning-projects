while True:
    number=int(input("Enter a number: (Only even numbers are allowed)"))
    if number%2==1:
        break
    print("The number is",number)
print("Wrong number :",number)

while True:
    number1=int(input("Enter a number: (Only even numbers are printed)"))
    if number1%2==1:
        continue
    print("The number is",number1)
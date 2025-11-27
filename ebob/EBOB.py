from sympy.physics.units import length


def ebob(num1,num2):
    range_length=min(num1,num2)

    ebob_num=0
    for i in range(1,range_length+1):
        if num1%i==0 and num2%i==0:
            ebob_num=i

    return ebob_num

while True:
    number1=int(input("Enter positive a number: "))
    number2=int(input("Enter positive a number: "))
    if number1>0 and number2>0:
        break
    else:
        print("Wrong number.")

print("EBOB({},{}) = {}".format(number1,number2,ebob(number1,number2)))
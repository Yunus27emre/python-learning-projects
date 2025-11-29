def dividers(number):
    list1=[]
    for num in range(1,number+1):
        if number % num == 0:
            list1.append(num)
    return list1

number = int(input("Enter a number: "))
print(dividers(number))
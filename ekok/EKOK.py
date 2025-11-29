def ekok(number1,number2):
  ekok_num=1
  for i in range(number1*number2,max(number1,number2)-1,-1):
        if i%number2==0 and i%number1==0:
          ekok_num=i
  return ekok_num

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print(ekok(num1,num2))

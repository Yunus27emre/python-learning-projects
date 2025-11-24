take=int(input("How many numbers will be taken?"))
list1=[]

for prime in range(2,take+1):
    is_prime = True
    for n in range(2,prime):
        if prime%n==0:
            is_prime=False
            break
    if is_prime:
        list1.append(prime)

print(list1)
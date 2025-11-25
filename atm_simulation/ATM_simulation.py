your_money=2000

choice=input("Press E to enter the card. ")

if choice=="E" or choice=="e":
    while True:
        operation=int(input("""
        Enter the operation:
         1-Withdraw Money
         2-Deposit Money
         3-Account Information
         4-Card Return"""))
        if operation==1:
            withdraw_money=int(input("Enter the money you want to withdraw: "))
            if withdraw_money>your_money:
                print("You don't have enough money")
            else:
                your_money-=withdraw_money

        if operation==2:
            deposit_money=int(input("Enter the money you want to deposit: "))
            your_money+=deposit_money

        if operation==3:
            print("Account Information:\nAccount Holder: Yunus Emre Taşkesen\nAccount IBAN:TR80 XXXX XXXX\nMoney Owned: {}".format(your_money))

        if operation==4:
            print("Card Return:\nCard Return Owned: {}".format(your_money))
            break
else:
    print("Invalid input")

class Bank:
    balance=1000
    def deposit(self,amount):
        if amount>0:
            Bank.balance+=amount
            print(f"{amount} Successfully Deposited!")
            print(f"New Account Balance: {Bank.balance}")
        else:
            print("Invalid Amount!")
    def withdraw(self,amount):
        if 0<amount<=Bank.balance:
            Bank.balance-=amount
            print(f"{amount} Successfully Withdrew!")
            print(f"New Account Balance: {Bank.balance}")
        else:
            print("Insufficient fund or Invalid Amount!")
    def checkBalance(self):
        print(f"Your Bank Balance: {Bank.balance}")
    def Exit(self):
        print("Thank You!! Visit Again..")

print("Welcome to Our Bank!!")
while True:
    account_num=int(input("Enter your Account Number: "))
    pin=int(input("Enter your PIN: "))
    if account_num==12345678 and pin==1234:
        print("Login Successful!!")
        break
    else:
        print("Oops! Invalid Account number or PIN.")

Account=Bank()
while True:
    print("\nSelect an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    option=int(input("Enter your Option: "))
    if option==1:
        amount=int(input("Enter the Amount to Deposit: "))
        Account.deposit(amount)
    elif option==2:
        amount=int(input("Enter the Amount to Withdraw: "))
        Account.withdraw(amount)
    elif option==3:
        Account.checkBalance()
    elif option==4:
        Account.Exit()
        break
    else:
        print("Invalid Input!! Please Try Again")


#Refer attached video for explanation






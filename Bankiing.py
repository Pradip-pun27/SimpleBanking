def My_balance(a):
    print("Yrs balance is :",a)
def deposit():
    amount1=int(input("Enter the amount wanna deposit:Rs."))
    print("u have deposited Rs.",amount1)
    return amount1
def withdraw(b):
    amount2=int(input("Enter amount wanna withdraw:Rs."))
    if amount2<b:
        print("Rs.",amount2," has been withdrawn. ")
        return amount2
    else:
        print("Insufficient balance.")
        return 0
    
def exit():
    print("************************************************************")
    print("                 Tysm for visiting us.                       ")
    print("************************************************************")

def main():
    balance=0
    value=True;
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("             Banking program in Python.                    ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" Enter 1. for balance inqury \n Enter 2. for deposit\n Enter 3.for withdraw\n Enter 4. for exit")
    print("-----------------------------------------------------------------")
   
    while value:
        ans=int(input("Enter number between 1-4:"))
        if ans==1:
            My_balance(balance)
        if ans==2:
            balance+=deposit()
            print(f"u have Rs.{balance} now.")
        if ans==3:
            balance-=withdraw(balance)
            print(f"u have Rs.{balance} now")
        if ans==4:
            exit()
            value=False
            
main()
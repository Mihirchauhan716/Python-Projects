

balance = 0

def deposit():
    global balance
    amt = float(input("Amount to deposit: "))
    balance += amt

def withdraw():
    global balance
    amt = float(input("Amount to withdraw: "))
    if amt <= balance:
        balance -= amt
    else:
        print("Not enough balance")

def check_balance():
    print("Balance:", balance)

deposit()
withdraw()
check_balance()

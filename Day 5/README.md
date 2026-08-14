# Bank Account Program

### Description

In today's lecture learn  about the class, object , method by using that created a simple bank Account program to understand the topics clearly.

Program allows to :
 
 created a user Account
 Store user values like user naem and balance
 Also update the Account balance

 ### Execution

 1. The Account created:





```bash
account = BankAccount('Datta', 5000)
```
account is created for datta and intitial balance is 5000

init method 



```bash
def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
```
2. Deposite money 

```bash
account.deposit(5000)
```
deposit method add money to account

```bash
def deposit(self, amount):
    self.balance += amount
```
Initial balance 5000 + 5000 = 10000

3.money withdraw and check if the balance is enough for withdraw
```bash
account.withdraw(1000)
```

```bash
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
    else:
        print("Insufficient balance")
```

4. Show balance
```bash
account.show_balance()   
```

```bash
def show_balance(self):
    print(f"Balance is :{self.balance}")   
```
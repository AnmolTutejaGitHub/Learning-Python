#object oriented programming
# For this challenge, create a bank account class that has two attributes:

# #owner
# #balance
# and two methods:

# #deposit
# #withdraw

# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

#sol...

class Account:
    def __init__ (self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amt):
        self.balance=self.balance+dep_amt
        print(f"Added{dep_amt} to the balance")

    def withdrawl(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print("Withdraw accepted")
        else:
            print("Sorry non enough funds")

    def __str__(self):
        return f"owner:{self.owner}\nBalance:{self.balance}"
    
a=Account("Sam",500)
print(a)

print(a.owner)
print(a.balance)
print(a)
a.deposit(100)
print(a)
a.withdrawl(600)

print(a)
a.withdrawl(1)






from collections.abc import Container
from multiprocessing.managers import Value
from pyclbr import Class


def exemple1():
    c1 = Account(1, 1, "Jonh", 0)
    c1.addValue(1000)
    c1.buildStatement()
    c1.withdraw(200)
    c1.buildStatement()

def exemple2():
    account1 = Account(1, 123, "John", 1000)
    withdraw = 300
    resultWithdraw = account1.withdraw(withdraw)

    if resultWithdraw:
        print(f"Withdraw of {withdraw}€ realized with success!")
        print(f"Current Balance: {account1.balance}€")
    else:
        print("Insufficient balance to withdraw")

def exemple3():
    c1 = Account(1, 123, "Peter", 1000)
    c2 = Account(2, 456, "Bree", 1000)

    c1 = c2

    c1.addValue(300)

    if c1 != c2:
        print("Differents memory address: ")
        print(f"{c1} \n {c2}")
    else:
        print("Equal memory address: ")
        print(f"{c1} \n {c2}")

    print(f"Account: {c1.number} \n Balance: {c1.balance}")
    print(f"Account: {c2.number} \n Balance: {c2.balance}")

class Account:
    def __init__(self, number, nif, namePrincipal, balance):
        self.number = number
        self.nif = nif
        self.namePrincipal = namePrincipal
        self.balance = balance

    def addValue(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def buildStatement(self):
        print(f"number: {self.number} \n nif: {self.nif} \n Balance: {self.balance}")

    def transferValue(self, destinationAccount, value):
        if self.balance < value:
            return ("Insufficient balance to this opperation")
        else:
            destinationAccount.addValue(value)
            self.withdraw(value)
            return ("Transfer done!")

def main():
    c1 = Account(1, 123, "Peter", 100)
    c2 = Account(2, 456, "Andrew", 300)
    print(f"Balance Account {c1.number}: {c1.balance}")
    print(f"Balance Account {c2.number}: {c2.balance}")

    print(c1.transferValue(c2, 80))
    print(f"Balance Account {c1.number}: {c1.balance}")
    print(f"Balance Account {c2.number}: {c2.balance}")

if __name__ == "__main__":
    main()
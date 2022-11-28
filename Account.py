class Account:
    def __init__(self, amount):
        self._balance = amount

    def setBalance(self, amount = 0):
        if amount > 0:
            self._balance = amount

    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw (self,amount):
        if amount > self._balance:
            return False
        else:
            self._balance -=amount
            return True
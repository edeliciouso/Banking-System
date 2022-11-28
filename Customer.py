from Account import Account
class Customer:
    def __init__(self,f,l):
        self._fName = f
        self._lName = l
        self._account = Account(0)

    def setAccount(self, account):
        self._account = account

    def setFirstName(self, f):
        self._fName = f

    def setLastName(self, l):
        self._lname = l

    def getFirstName(self):
        return self._fName

    def getLastName(self):
        return self._lName

    def getAccount(self):
        return self._account

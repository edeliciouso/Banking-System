from Customer import Customer
class Bank:
    def __init__(self,bName):
        self._bName = bName
        self._numOfCust = 0
        self._customers = []

    def addCustomer(self,f,l):
        self._customers.append(Customer(f,l))
        self._numOfCust += 1

    def getNumOfCust(self):
        return self._numOfCust

    def getCustomer(self,index):
        return self._customers[index]

    def editCustomer(self, index, f, l):
        self._customers[index].setFirstName(f)
        self._customers[index].setLastName(l)
        return self._customers[index]

    def deleteCustomer(self, index):
        if index > len(self._customers):
            return "ERROR"
        else:
            self._customers.pop(index)

    def searchCustomer(self,index,bName):
        return bName.getCustomer(index).getFirstName(), bName.getCustomer(index).getLastName()
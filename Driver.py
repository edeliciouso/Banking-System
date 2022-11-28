from Account import Account
from Customer import Customer
from Bank import Bank

b1 = Bank("BCA")
cus = []

def main():
    y = 1
    while y == 1:
        answer = int(input("Choose your role:\n 1. Administrator\n 2. Customer\n"))
        if answer == 1:
            print("Admin chosen.")
            adminAnswer()
        elif answer == 2:
            print("You are a Customer.")
            custAnswer()
        else:
            y += 1

def adminAnswer():
    option1 = int(input("What do you want to do?\n 1. Add customer\n 2. Delete customer\n 3. Edit customer\n 4. Search customer\n"))
    if option1 == 1: #add customer
        fName = input("Insert First Name: ")
        lName = input("Insert Last Name: ")
        b1.addCustomer(fName, lName)
        cus.append(fName + " " + lName)
    elif option1 == 2: #delete customer
        for x in cus:
            print(x)
        cusdelete = int(input("Insert number of customer you want to delete: "))
        cusindex = cusdelete - 1
        b1.deleteCustomer(cusindex)
        print("Successfully deleted.")
        cus.pop(cusindex)
    elif option1 == 3: #edit customer
        for x in cus:
            print(x)
        cusNumEdit = int(input("Insert number of customer you want to edit: "))
        fNewName = input("Insert Edited New First Name: ")
        lNewName = input("Insert Edited New Last Name: ")
        cusNameEdit = cusNumEdit - 1
        cus[cusNameEdit] = fNewName + " " + lNewName
        b1.editCustomer(cusNameEdit, fNewName, lNewName)
    elif option1 == 4: #search customer
        search = int(input("Insert number of customer you want to search: "))
        seacrhindex = search - 1
        print(cus[seacrhindex])
    else:
        return



def custAnswer():
    #deposit, withdraw, balance
    option2 = int(input("What do you want to do?\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n"))
    if option2 == 1:
        money = int(input("Insert customer number: "))
        moneyindex = money - 1
        print(b1.getCustomer(moneyindex).getAccount().getBalance())
    elif option2 == 2:
        money2 = int(input("Insert customer number: "))
        money2index = money2 - 1
        depo = int(input("Insert amount to deposit: "))
        print(b1.getCustomer(money2index).getAccount().deposit(depo))
        print("You've deposited " + str(depo))
    elif option2 == 3:
        money3 = int(input("Insert customer number: "))
        money3index = money3 - 1
        draw = int(input("Insert amount to withdraw: "))
        print(b1.getCustomer(money3index).getAccount().withdraw(draw))
        print("You've withdrawn " + str(draw))
        

if __name__ == "__main__":
    main()
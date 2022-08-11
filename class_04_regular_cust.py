class Customer:
    counter = 1000

    def __init__(self, phoneno, custname, add):
        Customer.counter += 1
        self.__customerid = Customer.counter
        self.__customername = custname
        self.__phonenumber = phoneno
        self.__address = add

    def setcustomerid(self, cid):
        self.__customerid = cid

    def setphonenumber(self, phno):
        self.__phonenumber = phno

    def getcustomerid(self):
        return self.__customerid

    def getphonenumber(self):
        return self.__phonenumber

    def getcustomername(self):
        return self.__customername

    def getaddress(self):
        return self.__address

    @staticmethod
    def gettotalcustomer():
        return Customer.counter-1000


class RegularCustomer(Customer):
    def __init__(self, phoneno, custname, discount, add):
        super().__init__(phoneno, custname, add)
        self.__discount = discount

    def setdiscount(self):
        self.__discount = dis

    def getdiscount(self):
        return self.__discount


class Address:
    def __init__(self, add):
        self.__addressline = add

    def setaddress(self, add):
        self.__addressline = add

    def getaddress(self):
        return self.__addressline


regcustadd1 = "Old cinema hall centre, MyVillage, AP-22222"
phoneno = 9999988888
regcustobj1 = RegularCustomer(phoneno, "coder", 5, regcustadd1)
print("customer ID: ", regcustobj1.getcustomerid())
print("Phone number: ", regcustobj1.getphonenumber())
print("Customer name: ", regcustobj1.getcustomername())
print("Discount: ", regcustobj1.getdiscount())
print("Customer's address: ", regcustobj1.getaddress())
print("\n")
print("Total customers registered: ", Customer.gettotalcustomer())

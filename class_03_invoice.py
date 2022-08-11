class Customer:
    counter = 1000

    def __init__(self, phoneno, custname, disc, add):
        Customer.counter += 1
        self.__customerid = Customer.counter
        self.__customername = custname
        self.__phonenumber = phoneno
        self.__address = add
        self.__discount = disc

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

    def getdiscount(self):
        return self.__discount

    @staticmethod
    def gettotalcustomer():
        return Customer.counter-1000


regcustadd1 = "Old cinema hall centre, MyTown, AP-000000"
phoneno = 9999977777
phone = 1234567890
addcust = "New cinema hall center, MyCity, AP-111111"
customer = Customer(phoneno, "Developer", 5, regcustadd1)
print("customer ID: ", customer.getcustomerid())
print("Phone number: ", customer.getphonenumber())
print("Customer name: ", customer.getcustomername())
print("Discount: ", customer.getdiscount())
print("Customer's address: ", customer.getaddress())
print("\n")
customer = Customer(phone, "programmer", 0, addcust)
print("cust id: ", customer.getcustomerid())
print("ph no: ", customer.getphonenumber())
print("add: ", customer.getaddress())
print("name: ", customer.getcustomername())
print("\n")
print("Total customers registered: ", Customer.gettotalcustomer())

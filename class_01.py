class Customer:
    counter = 1000
    def __init__(self):
        Customer.counter = Customer.counter + 1
        self.customerid = Customer.counter

    def setcustomerid(self, cid):
        self.customerid = cid

    def getcustomerid(self):
        return self.customerid

    @staticmethod
    def totalcustomers():
        return Customer.counter - 1000

obj = Customer()
print("Customer ID: ", obj.getcustomerid())
obj2 = Customer()
print("Customer ID: ", obj2.getcustomerid())
print("Total Customers: ", obj.totalcustomers())

class PrintDetails:
    def printheader(self, c, no=1):
        print(c * no)


class PurchaseBill:
    def __init__(self, bid, billamount):
        self.__billid = bid
        self.__billamount = billamount

    def getbillid(self):
        return self.__billid

    def getbillamount(self):
        return self.__billamount

    def calculatebill(self, mode, processcharge):
        if(mode == "credit"):
            self.__billamount += (self.__billamount * processcharge / 100)

    def displaybill(self):
        objprint = PrintDetails()
        objprint.printheader("-", 80)
        objprint.printheader("NN Retail Store Bill")
        objprint.printheader("-", 80)
        print("Bill ID: ", self.__billid)
        print("Final amount to be paid: Rs.", self.__billamount)
        objprint.printheader("-", 80)
        objprint.printheader("Thanks for Shopping")
        objprint.printheader("-", 80)


objpur = PurchaseBill(101, 1055.0)
objpur.calculatebill("credit", 10.5)
objpur.displaybill()

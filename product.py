class product:
    def __init__(self, price, item_name, weight, brand, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "Sold"
        return self
    def addtax(self):
        self.price*=0.15
        return self
    def returnitem(self, reason_for_return):
        self.reason_for_return = reason_for_return
        self.status = self.reason_for_return
        if self.status == "defective":
            self.price = 0
        elif self.status == "like_new":
            self.status = "for sale"
        elif self.status == "opened":
            self.status = "used"
            self.price*=0.8
        return self
    def displayinfo(self):
        print("Price:"+str(self.price), "Item Name:"+str(self.item_name),"weight:"+str(self.weight),"Brand:"+str(self.brand),"Status:"+str(self.status))
        return self

product1=product(4000,"DankShoes","300lb","MemeBrand")


product1.sell()
product1.returnitem("opened")
product1.displayinfo()
















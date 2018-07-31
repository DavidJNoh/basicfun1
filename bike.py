class bike:
        def __init__(self,price,max_speed,miles):
            self.price = price
            self.max_speed = max_speed
            self.miles = miles
        def displayinfo(self):
            print(self.price, self.max_speed, self.miles)
            return self
        def ride(self):
            print("Riding")
            self.miles+=10
            return self
        def reverse(self):
            if self.miles>=5:
                print("Reversing")
                self.miles-=5
                return self
            else:
                print("You can't reverse anymore")
                return self

bike1=bike(200,"25mph",0)

bike1.displayinfo()

bike1.ride().reverse().reverse().reverse().displayinfo().displayinfo()
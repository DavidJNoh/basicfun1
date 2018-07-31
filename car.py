class car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax=0.15
        else:
            self.tax=0.12
    def display_all(self):
        print("Price:"+str(self.price), "Speed:"+str(self.speed),"Fuel:"+str(self.fuel),"Mileage:"+str(self.mileage),"Tax:"+str(self.tax))
        return self

car1=car(2000,"35mph","Full","15mpg")
car2=car(2000,"5mph","Not Full","15mpg")
car3=car(2000,"15mph","Kind of Full","15mpg")
car4=car(2000,"25mph","Full","15mpg")
car5=car(2000,"45mph","Empty","15mpg")
car6=car(20000000,"35mph","Empty","15mpg")

car1.display_all()
class Car:
    def __init__(self, price, speed, fuel, mileage):
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.price = price
        self.speed = str(speed) + "mph"
        self.fuel = fuel
        self.mileage = str(mileage) + "mpg"
    def display_all(self):
        print(f"Price: {self.price}\nSpeed: {self.speed}\nFuel: {self.fuel}\nMileage: {self.mileage}\nTax: {self.tax}")
        return self

car1 = Car(2000,35,'Full',15)
car1.display_all()
car1 = Car(2000,5,'Full',105)
car1.display_all()
car1 = Car(2000,15,'Kind of Full',95)
car1.display_all()
car1 = Car(2000,25,'Full',25)
car1.display_all()
car1 = Car(2000,45,'Empty',25)
car1.display_all()
car1 = Car(20000000,35,'Empty',15)
car1.display_all()
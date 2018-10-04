class Bike:
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(f"Price: {self.price}, Maximum speed: {self.max_speed}, Total miles: {self.miles}")
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self

firstInstance = Bike(200, "25mph")
firstInstance.ride().ride().ride().reverse().displayInfo()
secondInstance = Bike(200, "25mph")
secondInstance.ride().ride().reverse().reverse().displayInfo()
thirdInstance = Bike(200, "25mph")
thirdInstance.reverse().reverse().reverse().displayInfo()

Add a check to the reverse method to see if miles > 5 before subtracting 5 from self.miles
displayInfo, ride, and reverse can return self
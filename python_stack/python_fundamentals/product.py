class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status ="for sale"
    def Sell(self):
        self.status = "sold"
        return self
    def AddTax(self, tax):
        self.price *= (1 + tax)
        return self
    def ReturnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price -= 0.2 * self.price
        return self
    def DisplayInfo(self):
        print(f"Price: {self.price}, Name: {self.item_name}, Weight: {self.weight}, Brand: {self.brand}, Status: {self.status}")
        return self
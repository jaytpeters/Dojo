class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print(self.health)
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a dragon")
        return self


lizard = Animal('Lizardry',10)
lizard.walk().walk().walk().run().run().displayHealth()
myDog = Dog("Doggo",200)
myDog.walk().walk().walk().run().run().pet().displayHealth()
myDragon = Dragon("FlyingRat",20)
myDragon.displayHealth()
newAnimal = Animal('Beast',20)
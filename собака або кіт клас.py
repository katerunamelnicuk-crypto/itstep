import random
class dog:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.happiness = 50
        self.is_alive = True
    def eat(self):
        print(f"{self.name} їсть")
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 10)
    def sleep(self):
        print(f"{self.name} спить")
        self.energy = 100
        self.hunger = min(100, self.hunger + 20)
    def play(self):
        if self.energy < 20:
            print(f"{self.name} змучений (або змучена)")
        phrase = "бігає за м'ячем"
        print(f"{self.name} {phrase}!")
        self.happiness = min(100, self.happiness + 25)
        self.energy -= 30
        self.hunger += 10
my_pet = dog("Дейзі")
print(my_pet)

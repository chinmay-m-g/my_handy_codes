class Automobiles:
    def __init__(self, model, price, yearm):
        self.model = model
        self.price = price
        self.yearm = yearm

    def increase_price(self):
        self.price = int(self.price * 1.1)
        print("Inside Automobiles Class")

    def get_price(self):
        print("Price of {model} is {price}".format(model=self.model, price=self.price))
        print("Inside the Automobile Class (Parent)")


class Car(Automobiles):
    def __init__(self, model, price, yearm, seats, roof_material):
        super().__init__(model, price, yearm)
        self.seats = seats
        self.roof_material = roof_material

    def increase_price(self):
        self.price = int(self.price * 2)
        print("Inside Car Class inherited from Automobiles")

    def get_price(self):
        print("Price of {model} is {price}".format(model=self.model, price=self.price))
        print("Inside the Car Class inherited from Automobile Class (Parent)")


class Bike(Automobiles):
    def __init__(self, model, price, yearm, stand_type, spoke_present):
        super().__init__(model, price, yearm)
        self.stand_type = stand_type
        self.spoke_present = spoke_present

    def increase_price(self):
        self.price = int(self.price * 5)
        print("Inside Bike Class inherited from Automobiles")


class SuperCar(Car):
    def __init__(self, model, price, yearm, seats, roof_material, cc, mileage):
        super().__init__(model, price, yearm, seats, roof_material)
        self.cc = cc
        self.mileage = mileage

    def increase_price(self):
        self.price = int(self.price * 6)
        print("Inside SuperCar Class inherited from 'Car' inherited from Automobiles")

    # def get_price(self):
    #     print("Price of {model} is {price}".format(model=self.model, price=self.price))


print("*" * 10 + "Super Car Class Initialization" + "*" * 10)
ferrari = SuperCar("ferrari", 100, 1995, 2, "steel", 2500, 10)

print("*" * 10 + "Increase price on Super Car instance" + "*" * 10)
ferrari.increase_price()

print("*" * 10 + "Get price on Super Car instance" + "*" * 10)
ferrari.get_price()

print("*" * 10 + "Defining a new value of price" + "*" * 10)
ferrari.price = 1500

print("*" * 10 + "Get price for tha instance of super class" + "*" * 10)
ferrari.get_price()

print(
    "*" * 10
    + "Calling the Super Class method using the child class instance"
    + "*" * 10
)
super(type(ferrari), ferrari).get_price()

print("*" * 10 + "Get help on any class" + "*" * 10)
print(help(SuperCar))

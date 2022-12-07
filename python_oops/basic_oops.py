class Car:
    def __init__(self, model, price, yearm):
        self.model = model
        self.price = price
        self.yearm = yearm

    def increase_price(self):
        self.price = int(self.price * 1.1)


honda = Car("City", 10, 2008)
tata = Car("Harrier", 15, 2020)

print("tata.model : ", tata.model)
print("tata.price : ", tata.price)
print("tata.yearm : ", tata.yearm)

print("*" * 50)

print("honda.model : ", honda.model)
print("honda.price : ", honda.price)
print("honda.yearm : ", honda.yearm)

print("*" * 50)
tata.increase_price()


print("tata.model : ", tata.model)
print("tata.price : ", tata.price)
print("tata.yearm : ", tata.yearm)

print("*" * 50)

print("honda.model : ", honda.model)
print("honda.price : ", honda.price)
print("honda.yearm : ", honda.yearm)

print("In new1 branch commit 3")

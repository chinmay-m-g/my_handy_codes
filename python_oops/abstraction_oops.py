from abc import ABC, abstractclassmethod

# https://www.youtube.com/watch?v=UDmJGvM-OUw


class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass


class Laptop(Computer):
    def function_1(self):
        print("Inside Laptop Class and function1")

    def function_1(self):
        print("Inside Laptop Class and function2")


class Mobile(Computer):
    def process(self):
        print("Inside the Mobile Class and process function")

    def function_1(self):
        print("Inside Mobile Class and function1")

    def function_1(self):
        print("Inside Mobile Class and function2")


# print("Creating Computer Object")
# comp_obj = Computer()

print("Creating Mobile Object")
mob_obj = Mobile()

# print("Creating Laptop Object")
# lap_obj = Laptop()



mynameisch> is a text
mynameisch> is a text
mynameisch> is a text
mynameisch> is a text
mynameisch> is a text
mynameisch> is a >
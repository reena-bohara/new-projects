from abc import ABC, abstractmethod

class coffee_processesor(ABC):
    @abstractmethod
    def heat_water(self):
        pass
    @abstractmethod
    def brew_coffee(self):
        pass
    
class CoffeeMachine(coffee_processesor):
    def __init__(self):
        self.__water_temperature = 0

    def make_coffee(self):
        self.heat_water()
        self.brew_coffee()

    def heat_water(self):
        self.__water_temperature = 100

    def brew_coffee(self):
        print("coffee is ready.")

machine = CoffeeMachine()
machine.make_coffee()
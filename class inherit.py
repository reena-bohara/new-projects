from abc import ABC, abstractmethod

class coffee_processesor(ABC):
    @abstractmethod
    def heat_water(self):
        pass
    @abstractmethod
    def brew_coffee(self):
        pass

class Tea_processesor(ABC):
    @abstractmethod
    def heat_water(self):
        pass
    @abstractmethod
    def brew_tea(self):
        pass

class DrinksMaker:
    def __init__(self,Sugar,CupSize):
        self.__waterML = 0
        self.__water_temperature = 0
        self.Sugar = Sugar
        self.CupSize = CupSize
    
class CoffeeMachine(coffee_processesor,DrinksMaker):
    def __init__(self,Sugar,CupSize, Coffee_percent, Coffee_type):
        super().__init__(Sugar,CupSize)
        self.Coffee_percent = Coffee_percent
        self.Coffee_type = Coffee_type

    def make_coffee(self):
        self.heat_water()
        self.brew_coffee()

    def heat_water(self):
        self.__water_temperature = 100

    def brew_coffee(self):
        print("coffee is ready.")

class TeaMachine(DrinksMaker,Tea_processesor):
    def __init__(self,Sugar,CupSize, Tea_percent, Tea_type):
        super().__init__(Sugar,CupSize)
        self.Tea_percent = Tea_percent
        self.Tea_type = Tea_type

    def make_Tea(self):
        self.heat_water()
        self.brew_tea()
        self.__water_temperature = 100
    def heat_water(self):
        self.__water_temperature = 100

    def brew_tea(self):
        print("Tea is ready.")

machine_1 = CoffeeMachine(5,"small", 60, "filtercoffee")
machine_1.make_coffee()
machine_2 = TeaMachine(5,"medium", 50, "strongtea")
machine_2.make_Tea()
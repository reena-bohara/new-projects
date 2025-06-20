from abc import ABC, abstractmethod

class SmartDevices(ABC):
    @abstractmethod
    def Devices(self):
        pass

class Items(SmartDevices):
    def __init__(self, brand, model_number, price, colour, regulator):
        self.brand = brand
        self.model_number = model_number
        self.price = price
        self.colour = colour
        self.regulator = regulator 

class SmartLight(SmartDevices, Items):
    def __init__(self,brand, model_number, price, colour, regulator):
        pass

class SmartThermoster(SmartDevices, Items):
    def __init__(self, brand, model_number, price, colour, regulator, temperature):
        super().__init__(temperature)
        self.__temperature = 24 

class SmartFan(SmartDevices, Items):
    def __init__(self, brand, model_number, price, colour, regulator):
        pass

    def Devices(SmartDevices):
        for Devices in SmartDevices:
            Devices()

    Devices = ['SmartLight'(), 'SmartThermoster'(), 'SmartFan'()]
    SmartDevices(Devices)
            
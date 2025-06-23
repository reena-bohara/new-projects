from abc import ABC, abstractmethod

class SmartDevices(ABC):
    @abstractmethod
    def activate(self):
        pass

class Items:
    def __init__(self, brand, model_number, price, colour, regulator):
        self.brand = brand
        self.model_number = model_number
        self.price = price
        self.colour = colour
        self.regulator = regulator 

class SmartLight(SmartDevices,Items):
    def __init__(self,brand, model_number, price, colour, regulator):
        super().__init__(brand, model_number, price, colour, regulator)
    def activate (self):
        print("Turn on the Lights")


class SmartThermostat(SmartDevices, Items):
    def __init__(self, brand, model_number, price, colour, regulator):
        super().__init__(brand, model_number, price, colour, regulator)
        self.__temperature = 24 
    def activate (self):
        print("Turn on the Thermostat")

class SmartFan(SmartDevices, Items):
    def __init__(self, brand, model_number, price, colour, regulator):
        super().__init__(brand, model_number, price, colour, regulator)
    def activate (self):
        print("Turn on the Fan")


def activate_devices(Electronics):
        for Devices in Electronics:
            Devices.activate()

Devices = [SmartLight('Bajaj','a1',4500,'white',3), SmartThermostat('Seimens', '301',2500,'cream',5), SmartFan('Cromtan','2B',1500,'Black',2)]
activate_devices(Devices)
            
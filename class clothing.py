class ClothingProduct:
    def __init__(self, name, price, colour, brand, size):
        self.name = name
        self.price = price
        self.colour = colour
        self.brand = brand
        self.size = size

    def payment(self):
        pass

class Shirting(ClothingProduct):
    def __init__(self,name, price, colour, brand, size, style):
        super().__init__(name, price, colour, brand, size)
        self.style = style
    def payment(self):
        pass

class HalfShirt(Shirting):
    def __init__(self, name, price, colour, brand, size, style, halfsleeves):
        super().__init__(name, price, colour, brand, size,style)
        self.halfsleeves = halfsleeves
    def payment(self):
        print("Received Payment Through UPI For HalfShirt")

class FullShirt(Shirting):
    def __init__(self, name, price, colour, brand, size, style, fullsleeves):
        super().__init__(name, price, colour, brand, size, style)
        self.fullsleeves = fullsleeves
    def payment(self):
        print("Received Payment Through UPI For FullShirt")

class TrackPant(ClothingProduct):
    def __init__(self,name, price, colour, brand, size,length):
        super().__init__(name, price, colour, brand, size,)
        self.length = length

class HalfPant(TrackPant):
    def __init__(self, name, price, colour, brand, size,length, kneesize):
        super().__init__(name, price, colour, brand, size,length)
        self.kneesize = kneesize

class FullPant(TrackPant):
    def __init__(self, name, price, colour, brand, size, length, anklesize):
        super().__init__(name, price, colour, brand, size, length)
        self.anklesize = anklesize

class T_Shirt(ClothingProduct):
    def __init__(self, name, price, colour, brand, size, fabric):
        super().__init__(name, price, colour, brand, size)
        self.fabric = fabric 

Cloth = HalfShirt('Zinc', 450, 'blue','Zinc cotton', 36, 'Chinese Collar', 14)
Cloth.payment()
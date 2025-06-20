from abc import ABC, abstractmethod

class paymentprocessor(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
    @abstractmethod
    def refund_payment(self, amount):
        pass

class PayPalprocessor(paymentprocessor):
    def __init__(self, balance):
        self.__balance = balance

    def make_payment(self, amount):
        self.__balance += amount
        print(f"Making Payment of ${amount:.2f}")
    
    def refund_payment(self, amount):
        if amount > self.__balance:
            print("ERROR Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Refunding Payment of ${amount:.2f}")


class CreditCardprocessor(paymentprocessor):
    def __init__(self, balance):
        self.__balance = balance

    def make_payment(self, amount):
        self.__balance += amount
        print(f"Making Payment of ${amount:.2f}")
    
    def refund_payment(self, amount):
        if amount > self.__balance:
            print("ERROR Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Refunding Payment of ${amount:.2f}")

class Netbankingprocessor(paymentprocessor):
    def __init__(self, balance):
        self.__balance = balance

    def make_payment(self, amount):
        self.__balance += amount
        print(f"Making Payment of ${amount:.2f}")
    
    def refund_payment(self, amount):
        if amount > self.__balance:
            print("ERROR Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Refunding Payment of ${amount:.2f}")

class Gpayprocessor(paymentprocessor):
    def __init__(self, balance):
        self.__balance = balance

    def make_payment(self, amount):
        self.__balance += amount
        print(f"Making Payment of ${amount:.2f}")
    
    def refund_payment(self, amount):
        if amount > self.__balance:
            print("ERROR Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Refunding Payment of ${amount:.2f}")

class PayTMprocessor(paymentprocessor):
    def __init__(self, balance = 80):
        self.__balance = balance

    def make_payment(self, amount):
        self.__balance += amount
        print(f"Making Payment of ${amount:.2f}")
    
    def refund_payment(self, amount):
        if amount > self.__balance:
            print("ERROR Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Refunding Payment of ${amount:.2f}")

 # Example
def checkout(processor, amount, choice):
    if choice.lower() == 'make':
        processor.make_payment(amount)
    elif choice.lower() == 'refund':
        processor.refund_payment(amount)
    else:
        print ("ERROR WRONG CHOICE")
        



checkout(PayPalprocessor(0), 500.00, "make")
checkout(CreditCardprocessor(50), 550.00, "Refund")
checkout(Netbankingprocessor(100), 300.00, "maek")
checkout(Gpayprocessor(10), 100.00, "Refund")
checkout(PayTMprocessor(), 150.00, "Make")
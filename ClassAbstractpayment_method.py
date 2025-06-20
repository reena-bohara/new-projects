from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

# Example
def checkout(processor, amount):
    processor.process_payment(amount)

checkout(CreditCardProcessor(), 100.00)
checkout(PayPalProcessor(), 150.50)
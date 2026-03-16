from abc import *
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
p1 = CreditCard()
p2 = UPI()
p1.pay(500)
p2.pay(1000)
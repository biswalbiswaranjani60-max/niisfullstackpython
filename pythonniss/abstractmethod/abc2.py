from abc import *
class Number(ABC):
    @abstractmethod
    def check(self, num):
        pass
class Prime(Number):
    def check(self, num):
        flag = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            print("Prime Number")
        else:
            print("Not a Prime Number")
n = int(input("Enter a number: "))
obj = Prime()
obj.check(n)
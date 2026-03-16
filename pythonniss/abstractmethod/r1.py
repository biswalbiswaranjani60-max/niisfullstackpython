from abc import *
class shape(ABC):
	def __init__(self,name):
		self.name=name
	@abstractmethod
	def area(self):
		pass
class Rectangle(shape):
	def __init__(self,n,l,b):
		super().__init__(n)
		self.l=l
		self.b=b
	def area(self):
		return self.l*self.b
class square(shape):
	def __init__(self,n,l):
		super().__init__(n)
		self.l=l
	def area(self):
		return self.l*self.l
r1=Rectangle("rect",5,7)
print(r1.area())
s1=square("sq",7)
print(s1.area())
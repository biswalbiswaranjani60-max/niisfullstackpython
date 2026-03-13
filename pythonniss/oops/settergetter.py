class student:
	def __init__(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def show(self):
		print("my name=",self.__name)
		print("my rollno=",self.__roll)
		print("my mark=",self.__mark)
	def update(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def set__Name(self,name):
		self.__name=name
	def set__Roll(self,roll):
		self.__roll=roll
	def set__Mark(self,mark):
		self.__mark=mark
	def get__Name(self):
		return self.__name
	def get__Roll(self):
		return self.__roll
	def get__Mark(self):
		return self.__mark
s=student("subha",1,90.50)
s.show()
s.update("subhamlenka",2,90.50)
s.show()
print("my name=",s.get__Name())





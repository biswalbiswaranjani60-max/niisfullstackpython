class student:
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name=value
s=student("subha")
print(s.name)
s.name=("lima")
print(s.name)
	
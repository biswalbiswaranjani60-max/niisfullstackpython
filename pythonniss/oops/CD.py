class demo:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")
d=demo()
print("hi")
demo()
print("hi")
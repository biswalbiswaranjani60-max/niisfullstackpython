class sical:
	def __init__(self,p,r,t):
		self.p=p
		self.time=t
		self.rate=r
	def show(self):
		print("principal=",self.p)
		print("time=",self.time)
		print("rate=",self.rate)
	def sical(self):
		return self.p*self.rate*self.time/100
print("enter principal, rate and time")
pr=float(input())
r=float(input())
t=float(input())
i1=sical(pr,r,t)
i1.show()
print("simple intrest=",i1.sical())


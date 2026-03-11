def sical(p,r,t):
	si=(p*r*t)/100
	return si
print("enter principal")
p=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
res=sical(p,r,t)
print("simpleintrest=",res)
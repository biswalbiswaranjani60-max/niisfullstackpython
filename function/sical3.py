def sical():
	print("enter principal")
	p=float(input())
	print("enter rate")
	r=float(input())
	print("enter time")
	t=float(input())
	SI=(p*r*t)/100
	return sical
res=sical()
print("simpleintrest=",res)
def facttest():
	print("enter a number")
	no=int(input())
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
res=facttest()
print("factorial=",res)


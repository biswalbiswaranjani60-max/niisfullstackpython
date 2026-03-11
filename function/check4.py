def check():
	print("enter a number")
	no=int(input())
	if no%2==0:
		return 0
	else:
		return 1
if check()==0:
	print("even number")
else:
	print("odd number")
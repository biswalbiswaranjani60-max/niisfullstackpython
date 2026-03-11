def check(no):
	print("enter a number")
	no=int(input())
	if no%2==0:
		return 0
	else:
		return 1
print("enter a number")
no=int(input())
print(check(no))
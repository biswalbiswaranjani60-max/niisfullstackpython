print("enter a number")
no=int(input())
if no<0:
	no=-no
if no<10:
	print("sd")
elif no<100:
	print("dd")
elif no<1000:
	print("td")
else:
	print("od")

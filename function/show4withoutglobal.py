def show(i):
	print("A")
	i=i+1
	if i<3:
		show(i+1)
	print("B")
def main():
	print("C")
	show(1)
	print("D")
main()

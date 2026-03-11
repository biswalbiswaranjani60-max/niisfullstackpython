i=1
def show():
	global i
	print("A")
	i=i+1
	if i<=3:
		show()
	print("B")
def main():
	print("C")
	show()
	print("D")
main()

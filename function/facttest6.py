def facttest(no):
	if no==0:
		return 1
	else:
		return no*facttest(no-1)
print(facttest(6))

import pickle
f=open("xyz.dat","rb")
while True:
	try:
		data=pickle.load(f)
		print(data)
	except EOFError:
		break
		f.close()
		
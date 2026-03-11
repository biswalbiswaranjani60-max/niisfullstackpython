def show(s):
	if len(s)==0:
		return s
	return show(s[1:])+s[0]
name="subhalima"
print(show(name))
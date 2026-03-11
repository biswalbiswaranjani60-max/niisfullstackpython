def cal(no1,no2):
	return no1+no2,no1-no2,no1*no2,no1//no2
print("enter tw0 no")
no1=int(input())
no2=int(input())
a,s,m,d=cal(no1,no2)
print("sum=",a)
print("sub=",s)
print("mult=",m)
print("div=",d)

print(f"sum=,{a},\nsub={s},\nmult={m},\ndiv={d}")
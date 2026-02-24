"""wap take emp salary from keyboard if sal>=5000 da=3% hra=20% then display basic salary da hra and total sal"""
print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)
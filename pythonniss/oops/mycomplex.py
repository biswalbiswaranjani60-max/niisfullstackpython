class MyComplex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
c1 = MyComplex(2, 4)
c2 = MyComplex(3, 5)
# c3 = c1 + c2   (error without operator overloading)
c3 = MyComplex(0, 0)
c3.r = c1.r + c2.r
c3.i = c1.i + c2.i
print(c1.r, "+", c1.i, "i")
print(c2.r, "+", c2.i, "i")
print(c3.r, "+", c3.i, "i")
class Student:
    def __init__(self, n, r, m):
        self.name = n
        self.roll = r
        self.mark = m
def show():
    s = Student("subha", 1, 50)
    return s
res = show()
print("My name:", res.name)
print("My roll:", res.roll)
print("My mark:", res.mark)
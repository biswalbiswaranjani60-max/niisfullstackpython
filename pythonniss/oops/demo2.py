class Student:
    def __init__(self, n,r,m):
        self.name =n
        self.roll =r
        self.mark =m
    def show(self):
        print("My name:", self.name)
        print("My roll:", self.roll)
        print("My mark:", self.mark)
s = Student("Lima", 1, 90)
s.show()

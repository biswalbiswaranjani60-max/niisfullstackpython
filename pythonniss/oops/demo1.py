class Demo:
    def __init__(self, n):
        self.n = n
        print("Constructor:", self.n)
    def __del__(self):
        print("Destructor:", self.n)
d1 = Demo("First")
d2 = Demo("Second")
d3 = Demo("Third")
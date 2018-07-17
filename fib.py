class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def next(self):
         self.a, self.b = self.b, self.a + self.b
         return self.a

for i, f in enumerate(Fib()):
    print f
    if i > 10:
        break



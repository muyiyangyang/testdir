class stack(object):
    def __init__(self):
        self.stack = []

    def isfull(self):
        return self.stack == []

    def push(self, m):
        self.stack.append(m)

    def pop(self):
        if not self.isfull():
            self.stack.pop()

    def show(self):
        print self.stack

s = stack()
s.push(2)
s.show()
s.push(3)
s.show()
s.push(4)
s.show()
s.push(5)
s.show()
s.pop()
s.show()
s.pop()
s.show()
s.pop()
s.show()


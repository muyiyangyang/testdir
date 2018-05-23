class queue(object):
    def __init__(self):
        self.queue = []

    def isfull(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def push(self, m):
        self.queue.append(m)

    def pop(self):
        if not self.isfull():
            self.queue.pop(0)

    def show(self):
        print self.queue

s = queue()
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

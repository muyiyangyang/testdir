class Stack():
    def __init__(self):
        self.stack = []

    def empty(self):
        return self.stack == []
   
    def clear(self):
        del self.stack[:]
   
    def show(self):
        return self.stack[:]
   
    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
        
    def top(self):
        return self.stack[self.size() -1]

s = Stack()
s.push(8)
s.push(9)
s.push(10)
s.push(11)
print s.show()
print s.size()
if not s.empty():
    print 11
    s.pop()
print s.show()
print s.size()
if not s.empty():
    print 22
    s.pop()
print s.show()
print s.size()
if not s.empty():
    print 33
    s.pop()
print s.show()
print s.size()
if not s.empty():
    print 44
    s.pop()
print s.show()
print s.size()
if not s.empty():
    print 55
    s.pop()
print s.show()
print s.size()

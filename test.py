def genipport(iplist, portlist):
    #IPs = genip(iplist)
    IPs = (iplist)
    for ip in IPs:
        #Ports = genport(portlist)
        Ports = (portlist)
        for port in Ports:
            yield (ip,port)

IPList = [11,2,32,435,2,3,55,6,5,4,443,333,2244,55]
PortList = [11,4,4,555,6,67777,7664,33,22,223,44,44,44]
ipWITHport = genipport(IPList, PortList)  
item = next(ipWITHport) 
#print item

def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

#print fab(12)

def fab1(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, b + a
    n = n + 1

f = fab1(5)
#  print n

class Fab(object):
  def __init__(self, max):
    self.max = max
    self.n, self.a, self.b = 0, 0, 1

  def __inter__(self):
    return self

  def next(self):
    if self.n < self.max:
      r = self.b
      self.a, self.b = self.b, self.a + self.b
      self.n = self.n + 1
      return r
    raise StopIteration()


def read_file(fpath):
  BLOCK_SIZE = 10
  with open(fpath, 'rb') as f:
    while True:
      #block = f.read(BLOCK_SIZE)
      block = f.readline()
      if block:
        yield block
      else:
        return

data = read_file('/root/test.py')
for d in data:
  print d
  print 111111111111111111

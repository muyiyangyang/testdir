from Queue import Queue  
  
class Node:  
    def __init__(self,value=None,left=None,right=None):  
        self.value=value  
        self.left=left  
        self.right=right 

def hight(tree):
    if not tree:
        return 0
    lefth = hight(tree.left)
    righth = hight(tree.right)
    if lefth > righth:
        return lefth + 1
    else:
        return righth + 1

root = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

q = Queue()
print q.put(root)
print root
print root.left.left
print root.right
print hight(root)

import queue2

class Node(object):
    
    def __init__(self,key,parent=None):
        self.key = key
        self.data = None
        self.parent = parent
        self.lchild = None
        self.rchild = None

    def add_lchild(self,node):
        self.lchild = node
        node.parent = self

    def add_rchild(self,node):
        self.rchild = node
        node.parent = self

    def has_lchild(self):
        return self.lchild != None

    def has_rchild(self):
        return self.rchild != None

    def is_leaf(self):
        return (self.lchild == None and
                self.rchild == None)

    def pre_order(self):
        print(self.key)
        if self.has_lchild():
            self.lchild.pre_order()
        if self.has_rchild():
            self.rchild.pre_order()

    def in_order(self):
        if self.has_lchild():
            self.lchild.in_order()
        print(self.key)
        if self.has_rchild():
            self.rchild.in_order()
        
    def post_order(self):
        if self.has_lchild():
            self.lchild.post_order()
        if self.has_rchild():
            self.rchild.post_order()
        print(self.key)

    def breadth_first(self):
        q = queue2.Queue(self)
        
        while not q.is_empty():
            node = q.dequeue()
            print(str(node.key))
            if node.has_lchild():
                q.enqueue(node.lchild)
            if node.has_rchild():
                q.enqueue(node.rchild)
      

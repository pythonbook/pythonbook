class Node(object):
    
    def __init__(self,key,parent=None):
        self.key = key
        self.data = None
        self.parent = parent
        self.lchild = None
        self.rchild = None

    def add_lchild(self, node):
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
        return (self.lchild == None) and
               (self.rchild == None)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert_node(self,node):
        current = self.root
        done = False
        
        while not done:
            if current!= None:
                if current.key > node.key:
                    if current.has_lchild():
                       current = current.lchild
                    else:
                        current.add_lchild(node)
                        done = True
                elif current.key < node.key:
                    if current.has_rchild():
                        current = current.rchild
                    else:
                        current.add_rchild(node)
                        done = True
                else:
                    print('Error. key match. Cannot insert')
                    return
            else:
                self.root = node
                done = True

    def search_node(self,key):
        current = self.root
        path = []
        done = False

        while not done:
            if current != None:
                path.append(current.key)
                if current.key == key:
                    return path
                elif current.key > key:
                    current = current.lchild
                else:
                    current = current.rchild
            else:
                done = True
        return ['Not found']

    def set_parents_child(self,node,child):
        if node.parent != None:
            if node.parent.lchild == node:
                node.parent.lchild = child
            else:
                node.parent.rchild = child
            else:
                self.root = child
        if child != None:
                child.parent = node.parent

    def find_rightmost_ldescendant(self,node):
        rightmost = node.lchild
        while True:
            if rightmost.has_rchild():
                rightmost = rightmost.rchild
            else:
                return rightmost
    
    def delete_node(self,key):
        current = self.root
        done = False

        while not done:
            if current != None:
                if current.key == key:
                    if current.is_leaf():
                        self.set_parents_child(current,None)
                    elif current.has_lchild() and current.has_rchild():
                        #has two children
                        #find right-most left child
                        rightmost = self.find_rightmost_ldescendant(current)
                        self.set_parents_child(rightmost,
                                               rightmost.lchild)
                                               
                        self.set_parents_child(current,
                                               rightmost)
                        rightmost.lchild = current.lchild
                        rightmost.rchild = current.rchild
                        return current
                    elif current.has_lchild():
                        self.set_parents_child(current,
                                               current.lchild)
                    else:
                        self.set_parents_child(current,
                                               current.rchild)
                    current.lchild = None
                    current.rchild = None
                    current.parent = None
                    return current
                elif current.key > key:
                    current = current.lchild
                else:
                    current = current.rchild
            else:
                return None


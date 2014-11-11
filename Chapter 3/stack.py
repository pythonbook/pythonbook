class Stack(object):
    def __init__(self,element=None):
        self.elements = []
        if element != None:
            self.elements.append(element)

    def push(self,element):
        self.elements.append(element)
    
    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            return None

    def top(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            return None

    def is_empty(self):
        return len(self.elements) == 0

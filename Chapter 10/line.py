class Line(object):
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        if a[0] != b[0]:
            self.m = (a[1]-b[1])/(a[0]-b[0])
            self.C = (a[1]*b[0]-b[1]*a[0])/(a[0]-b[0])
        else:
            self.m = float('inf')
            self.X = a[0]

    def is_in_line(self,a):
        if self.m != float('inf'):
            return a[1] == self.m * a[0] + self.C
        else:
            return a[0] == self.X

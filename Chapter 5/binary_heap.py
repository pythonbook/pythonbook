class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        

class Heap(object):
    def __init__(self):
        self.list = []

    def insert(self,element):
        #location of last element
        self.list.append(element)
        loc = len(self.list) -1
    
        done = False
        while not done:
            if loc == 0:
                self.list[loc] = element
                return
            if self.list[loc//2].key < element.key:
                self.list[loc] = self.list[loc//2]
                loc = loc//2
            else:
                self.list[loc] = element
        return

    def delete(self):
        if len(self.list) == 0:
            print('No element to delete')
            return
      
        retval = self.list[0]
        lastelt = self.list.pop()

        if retval == lastelt:
            return retval
    
        loc = 0
        done = False

        while not done:
            lc = 2 * loc+1
            rc = 2 * loc+2
            maxindex = loc
            self.list[loc] = lastelt
      
            if lc < len(self.list):
                if self.list[lc].key > lastelt.key:
                    maxindex = lc
            if rc < len(self.list):
                if self.list[rc].key > self.list[maxindex].key:
                    maxindex = rc
            if maxindex != loc:
                self.list[loc] = self.list[maxindex]
                loc = maxindex
            else:
                return retval
      
    def print_heap(self):
        print("**********")
        for n in self.list:
            print(str(n.key))
        print('---------')
    
    

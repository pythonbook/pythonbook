import queue2

class Node(object):
    
    def __init__(self,index,data=None):
        self.data = data
        self.index = index
        self.edges = []
        self.visited = False

    def add_edge(self,node):
        if node not in self.edges:
            self.edges.append(node)

    def delete_edge(self,node):
        if node in self.edges:
            self.edges.remove(node)

    def is_edge(self,node):
        return node in self.edges
  
    def set_visited(self,val):
        self.visited = val
    
    def set_data(self,data):
        self.data = data
    
    def print_edges(self):
        E=[]
        for v in self.edges:
            E.append((self.index,v.index))
        print(E)

    def depth_first_traverse(self):
        if self.visited:
            return
        self.visited = True
        print(str(self.data))
        for adj in self.edges:
            adj.depth_first_traverse()
      
    def breadth_first_traverse(self, q):
        for adj in self.edges:
            if not adj.visited:
                adj.visited = True
                q.enqueue(adj)
        
class Graph(object):
    
    def __init__(self,num_vertices):
        self.nodes = []
        for i in range(num_vertices):
            self.nodes.append(Node(i))

    def set_node_data(self,u,data):
        if u < len(self.nodes):
            self.nodes[u].data=data
        else:
            print('Incorrect vertex number')

    def add_edge(self,u,v):
        if (u < len(self.nodes) and
            v < len(self.nodes)):
            if (self.nodes[u].is_edge(self.nodes[v]) or
                self.nodes[v].is_edge(self.nodes[u])):
                print('Duplicate edge (' +
                      str(u)+','+str(v)+')')
            else:
                self.nodes[u].add_edge(self.nodes[v])
                self.nodes[v].add_edge(self.nodes[u])
        else:
            print('Incorrect vertex number')
  
    def delete_edge(self,u,v):
        if u < len(self.nodes) and v < len(self.nodes):
            self.nodes[u].delete_edge(self.nodes[v])
            self.nodes[v].delete_edge(self.nodes[u])
        else:
            print('Incorrect vertex number')
 
    def get_node_number(self,data):
        #this code assumes data is unique
        #modifying this code to handle non-unique
        #data is an exercise.
        for i in range(len(self.nodes)):
            if self.nodes[i].data == data:
                   return self.nodes[i].index
        return None

    def print_graph(self):
        for i in range(len(self.nodes)):
            print('Node number: ' + str(i) +
                  ' data: ' + str(self.nodes[i].data))
            self.nodes[i].print_edges()

    def depth_first_traverse(self):
        if len(self.nodes) > 0:
            self.nodes[0].depth_first_traverse()

    def depth_first_traverse2(self):
        for node in self.nodes:
            node.depth_first_traverse()
  
    def breadth_first_traverse(self):
        q = queue2.Queue()
        for node in self.nodes:
            if not node.visited:
                node.visited=True
                q.enqueue(node)
                while not q.is_empty():
                    curnode = q.dequeue()
                    print(str(curnode.data))
                    curnode.breadth_first_traverse(q)
          
      

class Node(object):
    
    def __init__(self,index,data=None):
        self.data = data
        self.index = index
        self.visited = False

    def set_visited(self,val):
        self.visited = val
    
    def set_data(self,data):
        self.data = data

class Graph(object):
    
    def __init__(self,num_vertices):
        self.nodes=[]
        self.matrix = [[0 for i in range(num_vertices)] \
                       for j in range(num_vertices)]

        for i in range(num_vertices):
            self.nodes.append(Node(i))

    def set_vertex(self,u,data):
        if u < len(self.nodes):
            self.nodes[u].data=data
        else:
            print('Incorrect vertex number')

    def add_edge(self, u, v):
        if (u < len(self.nodes) and
            v < len(self.nodes)):
            self.matrix[u][v]=1
            self.matrix[v][u]=1
        else:
            print('Incorrect vertex number')

    def delete_edge(self, u, v):
        if (u < len(self.nodes) and
            v < len(self.nodes)):
            self.matrix[u][v] = 0
            self.matrix[v][u] = 0
        else:
            print('Incorrect vertex number')

    def get_node_number(self,data):
        for i in range(len(self.nodes)):
            if self.nodes[i].data == data:
                return self.nodes[i].index
        return None

    def print_graph(self):
        for i in range(len(self.nodes)):
            print('Node number: '+ str(i) +
                  ' data: '+str(self.nodes[i].data))
            adjlist = []
            for j in range(len(self.nodes)):
                if self.matrix[i][j] == 1:
                    adjlist.append((i,j))
            print(adjlist)
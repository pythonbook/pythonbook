import weighted_graph
import graph_priority_queue

class NodeData(object):
    def __init__(self,vertex,Svertex,weight):
        self.vertex = vertex
        self.Svertex = Svertex
        self.weight = weight
        
def dijkstra(G,s):
    span_tree = weighted_graph.Graph(G.num_nodes())
    in_span_tree = [False]*G.num_nodes()
    distances = [float('inf')]*G.num_nodes()
    distances[s] = 0
    predecessors = [-1]*G.num_nodes()
    E = []
    graph_PQ = graph_priority_queue.MinHeap(G.num_nodes())
    for v in range(G.num_nodes()):
        E.extend(G.get_node(v).get_edges())

    source = NodeData(s,-1,0)
    graph_PQ.insert(source)

    while not graph_PQ.is_empty():
        element = graph_PQ.pop()
        span_tree.set_vertex(element.vertex,
                         G.get_node(element.vertex).data)
        in_span_tree[element.vertex] = True
        
        if element.Svertex != -1:
            span_tree.add_edge(element.vertex,
                           element.Svertex,
                           element.weight)
        
        adjlist = G.get_node(element.vertex).get_edges()

        for Svertex, candidate_vertex, wt in adjlist:
            if in_span_tree[candidate_vertex] == False:
                if (distances[candidate_vertex] >
                   (distances[Svertex] + wt)):
                       
                    predecessors[candidate_vertex] = Svertex
                    distances[candidate_vertex] = distances[Svertex]+wt
                    
                    newelt = NodeData(candidate_vertex,
                                      Svertex,
                                      distances[candidate_vertex])
                    graph_PQ.insert(newelt)

    for v in range(G.num_nodes()):
        if v == s:
            continue
        if (predecessors[v]==-1 or
            distances[v] == float('inf')):
            print('NO PATH from node '+ str(s) +
                  ' to node '+ str(v))
            continue
        else:
            print('Shortest path (cost = '+ str(distances[v])+
                  ') from node '+str(s)+' to node '+str(v)+': ')
        stack = [v]
        done = False
        current_node = v

        while not done:
            current_node = predecessors[current_node]
            if current_node != -1:
                stack.append(current_node)
            else:
                done = True
        stack.reverse()
        print(stack)

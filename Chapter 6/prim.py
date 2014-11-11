import graph_priority_queue
import weighted_graph

class NodeData(object):
    def __init__(self,vertex,MST_vertex,weight):
        self.vertex = vertex
        self.MST_vertex = MST_vertex
        self.weight = weight

def prim(G,root):
    MST = weighted_graph.Graph(G.num_nodes())
    inMST = [False]*G.num_nodes()
    graph_PQ = graph_priority_queue.MinHeap(G.num_nodes())
    root_node = NodeData(root,root,0)
    graph_PQ.insert(root_node)
    MSTwt = 0
    
    while not graph_PQ.is_empty():
        element = graph_PQ.pop()
        
        MST.set_vertex(element.vertex,
                       G.get_node(element.vertex).data)
                       
        inMST[element.vertex] = True
        
        if element.vertex != element.MST_vertex:
            MST.add_edge(element.vertex,
                        element.MST_vertex,
                        element.weight)
                        
            MSTwt = MSTwt + element.weight
        adjlist = G.get_node(element.vertex).get_edges()
        
        for MST_vertex, candidate_vertex, wt in adjlist:
            if not inMST[candidate_vertex]:
                newelt = NodeData(candidate_vertex,
                                  MST_vertex,wt)
                graph_PQ.insert(newelt)

    print('MST weight: ' + str(MSTwt))
    return MST
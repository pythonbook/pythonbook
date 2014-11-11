import weighted_graph
import kruskal

node_numbers = {'John':0, 'Sally':1, 'George':2,
               'Phil':3, 'Rose':4, 'Alice':5}

G = weighted_graph.Graph(len(node_numbers))
for node in node_numbers:
  G.set_vertex(node_numbers[node],node)

G.add_edge(node_numbers['John'],node_numbers['Sally'],1)
G.add_edge(node_numbers['John'],node_numbers['George'],2)
G.add_edge(node_numbers['John'],node_numbers['Rose'],3)
G.add_edge(node_numbers['George'],node_numbers['Sally'],4)
G.add_edge(node_numbers['Phil'],node_numbers['Sally'],5)
G.add_edge(node_numbers['Rose'],node_numbers['Alice'],6)

G.print_graph()

print('Breadth First Traversal:')
G.breadth_first_traverse()

MST = kruskal.kruskal(G)
MST.print_graph()
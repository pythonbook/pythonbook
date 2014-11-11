import weighted_graph
import floyd_warshall

node_numbers = {'N1':0, 'N2':1, 'N3':2, 'N4':3,
               'N5':4, 'N6':5, 'N7':6, 'N8':7}

G = weighted_graph.Graph(len(node_numbers))
for node in node_numbers:
  G.set_vertex(node_numbers[node],node)

G.add_edge(node_numbers['N1'],node_numbers['N2'],3)
G.add_edge(node_numbers['N1'],node_numbers['N4'],2)
G.add_edge(node_numbers['N1'],node_numbers['N3'],3)

G.add_edge(node_numbers['N2'],node_numbers['N4'],9)
G.add_edge(node_numbers['N2'],node_numbers['N5'],4)
G.add_edge(node_numbers['N2'],node_numbers['N7'],2)

G.add_edge(node_numbers['N3'],node_numbers['N4'],-4)
G.add_edge(node_numbers['N3'],node_numbers['N5'],1)
G.add_edge(node_numbers['N3'],node_numbers['N7'],6)
G.add_edge(node_numbers['N3'],node_numbers['N8'],6)

G.add_edge(node_numbers['N4'],node_numbers['N6'],1)

G.add_edge(node_numbers['N5'],node_numbers['N7'],7)

floyd_warshall.floyd_warshall(G)

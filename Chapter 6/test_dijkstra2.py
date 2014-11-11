import weighted_graph
import dijkstra
import prim

node_numbers = {'N1':0, 'N2':1, 'N3':2, 'N4':3}

G = weighted_graph.Graph(len(node_numbers))
for node in node_numbers:
  G.set_vertex(node_numbers[node],node)

G.add_edge(node_numbers['N1'],node_numbers['N2'],2)
G.add_edge(node_numbers['N1'],node_numbers['N4'],2)
G.add_edge(node_numbers['N2'],node_numbers['N3'],2)
G.add_edge(node_numbers['N3'],node_numbers['N4'],-4)

G.print_graph()

dijkstra.dijkstra(G,node_numbers['N1'])

print('****')

MST = prim.prim(G,node_numbers['N1'])
MST.print_graph()

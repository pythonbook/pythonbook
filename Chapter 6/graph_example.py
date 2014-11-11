import graph

node_numbers = {'John':0, 'Sally':1, 'George':2,
               'Phil':3, 'Rose':4, 'Alice':5}

G = graph.Graph(len(node_numbers))
for node in node_numbers:
  G.set_node_data(node_numbers[node],node)

G.add_edge(node_numbers['John'],node_numbers['Sally'])
G.add_edge(node_numbers['John'],node_numbers['George'])
G.add_edge(node_numbers['John'],node_numbers['Rose'])
G.add_edge(node_numbers['George'],node_numbers['Sally'])
G.add_edge(node_numbers['Phil'],node_numbers['Sally'])
G.add_edge(node_numbers['Rose'],node_numbers['Alice'])

G.print_graph()

print('Breadth First Traversal:')
G.breadth_first_traverse()
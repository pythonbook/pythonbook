import graph

def depth_first_traverse(node):
    if node.visited:
        return
    node.visited = True
    print(str(node.data))
    for adj in node.get_adjacent_nodes():
        depth_first_traverse(adj)

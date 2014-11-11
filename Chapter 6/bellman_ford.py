import weighted_graph

def bellman_ford(G,s):
    distances = [float('inf')]*G.num_nodes()
    distances[s] = 0
    predecessors = [-1]*G.num_nodes()
    E = []
    for v in range(G.num_nodes()):
        E.extend(G.get_node(v).get_edges())
    
    for iter in range(G.num_nodes()-1):
        for u, v, w in E:
            if distances[v] > (distances[u] + w):
                predecessors[v] = u
                distances[v] = distances[u]+w
    for u,v,w in E:
        if distances[v] > (distances[u] + w):
                distances[v] = float('-inf')

    for v in range(G.num_nodes()):
        if v == s:
            continue
        if (predecessors[v] == -1 or
            distances[v] == float('-inf')):
            print('NO PATH from node '+ str(s) +
                  ' to node '+str(v))
            continue
        else:
            print('Shortest path (cost = '+
                  str(distances[v]) +
                  ') from node '+ str(s)+
                  ' to node '+str(v)+': ')
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
import weighted_graph

def floyd_warshall(G):
    distances = [[float('inf') for i in range(G.num_nodes())]
                 for j in range(G.num_nodes())]
    
    for i in range(G.num_nodes()):
        distances[i][i]=0
    predecessors = [[-1 for i in range(G.num_nodes())]
                    for j in range(G.num_nodes())]
    
    E = []
    for v in range(G.num_nodes()):
        E.extend(G.get_node(v).get_edges())

    for u, v, w in E:
        predecessors[u][v] = u
        distances[u][v] = w
    
    for k in range(G.num_nodes()):
        for i in range(G.num_nodes()):
            for j in range(G.num_nodes()):
                newdist = distances[i][k]+distances[k][j]
                if newdist < distances[i][j]:
                    distances[i][j] = newdist
                    predecessors[i][j] = predecessors[k][j]

    for v in range(G.num_nodes()):
        for u in range(G.num_nodes()):
            if v == u:
                if predecessors[u][v] != -1:
                    print('There is a negative cycle in '
                          'the graph that includes vertex '+
                          str(u))
                continue
            if predecessors[u][u] != -1:
                print('There is a negative cycle in '
                      'the path from '+ str(u) +
                      ' to ' + str(v))
                continue
            elif distances[u][v] == float('inf'):
                print('NO PATH from node '+str(u) +
                      ' to node '+ str(v))
                continue
            else:
                print('Shortest path (cost = '+
                      str(distances[u][v]) +
                      ') from node '+ str(u) +
                      ' to node '+ str(v)+': ')
            stack = [v]
            done = False
            current_node = v

            while not done:
                current_node = predecessors[u][current_node]
                if current_node != -1:
                    stack.append(current_node)
                else:
                    done = True
            stack.reverse()
            print(stack)

        
            

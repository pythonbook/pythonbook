import weighted_graph

def initialize_set(n):
    parent =[0] * n
    for i in range(n):
        parent[i] = -1
    return parent

def find_root(S,n):
    root = n
    while S[root] > 0:
        root = S[root]

    if(S[n]>0):
        S[n] = root
    return root

def union(S,root1,root2):
    if S[root1] < S[root2]:
        S[root2] = root1
    elif S[root2] < S[root1]:
        S[root1] = root2
    else:
        S[root1] = root2
        S[root2] = S[root2]-1
    

def kruskal(G):
    set_roots = initialize_set(G.num_nodes())
    MST = weighted_graph.Graph(G.num_nodes())
    for i in range(G.num_nodes()):
        MST.set_vertex(i,G.get_node(i).data)
    E = G.sort_edges()
    MSTwt = 0
    for i in range(len(E)):
        u, v, w = E[i]
        rootu = find_root(set_roots,u)
        rootv = find_root(set_roots,v)

        if rootu != rootv:
            union(set_roots,rootu,rootv)
            print('Adding edge: ' + str((u,v,w)))
            MST.add_edge(u,v,w)
            MSTwt = MSTwt+w
    print('MST weight: ' + str(MSTwt))
    return MST
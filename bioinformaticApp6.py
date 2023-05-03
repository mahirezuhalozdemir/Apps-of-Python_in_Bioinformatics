import networkx as nx
G = nx.Graph()

#G.add_node(1)

#G.add_nodes_from([2, 3])
"""
H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from(H.edges)
"""
"""
G.clear()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(G.number_of_nodes())
print(G.number_of_edges())

DG = nx.DiGraph()
DG.add_edge(2, 1)   # adds the nodes in order 2, 1
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]

print(list(DG.nodes))

print(list(DG.edges))

print(list(DG.adj[1]))  # or list(G.neighbors(1))

print(DG.degree[1])  # the number of edges incident to 1
"""


G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

#print(list(G.nodes))
G.remove_node(2)
G.remove_nodes_from("spam")
G.remove_edge(1, 3)
#print(list(G.nodes))


G.add_edge(1, 2)
H = nx.DiGraph(G)  # create a DiGraph using the connections from G
#print(list(H.edges())) #[(1, 2), (2, 1)]
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)  # create a graph from an edge list
#print(list(H.edges())) #[(0, 1), (1, 2), (2, 3)]
adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
H = nx.Graph(adjacency_dict)  # create a Graph dict mapping nodes to nbrs
#print(list(H.edges())) #[(0, 1), (0, 2), (1, 2)]

G = nx.Graph([(1, 2, {"color": "yellow"})])
#print(G[1]) # same as G.adj[1] --> {2: {'color': 'yellow'}}
#print(G[1][2]) #{'color': 'yellow'}
#print(G.edges[1, 2]) #{'color': 'yellow'}

G.add_edge(1, 3)
G[1][3]['color'] = "blue"
G.edges[1, 2]['color'] = "red"
#print(G.edges[1, 2]) #{'color': 'red'}

FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in FG.adj.items():
   for nbr, eattr in nbrs.items():
       wt = eattr['weight']
       #if wt < 0.5: print(f"({n}, {nbr}, {wt:.3})")
"""
for (u, v, wt) in FG.edges.data('weight'):
    if wt < 0.2:
        print(f"({u}, {v}, {wt:.3})")
"""

G = nx.Graph(day="Friday")
#print(G.graph)
G.graph['day'] = "Monday"
#print(G.graph)

G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
#print(G.nodes[1])

G.nodes[1]['room'] = 714
#print(G.nodes.data())

G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edges[3, 4]['weight'] = 4.2
#print(G.edges.data())

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
#print(DG.out_degree(1, weight='weight')) #0.5

#print(DG.degree(1, weight='weight')) #1.25

#print(list(DG.successors(1))) #[2]

#print(list(DG.neighbors(1))) #[2]

H = nx.Graph(G)  # create an undirected graph H from a directed graph G

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
#print(dict(MG.degree(weight='weight'))) #{1: 1.25, 2: 1.75, 3: 0.5}

GG = nx.Graph()
for n, nbrs in MG.adjacency():
   for nbr, edict in nbrs.items():
       minvalue = min([d['weight'] for d in edict.values()])
       GG.add_edge(n, nbr, weight = minvalue)

#print(nx.shortest_path(GG, 1, 3)) #[1, 2, 3]


K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)
""" 
print(K_5)
print(K_3_5)
print(barbell)
print(lollipop)
"""

er = nx.erdos_renyi_graph(100, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(100, 5)
red = nx.random_lobster(100, 0.9, 0.9)
#print(er)
#print(ws)
#print(ba)
#print(red)

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node("spam")       # adds node "spam"
#print(list(nx.connected_components(G))) #[{1, 2, 3}, {'spam'}]

#print(sorted(d for n, d in G.degree())) #[0, 1, 1, 2]

#print(nx.clustering(G)) #{1: 0, 2: 0, 3: 0, 'spam': 0}

sp = dict(nx.all_pairs_shortest_path(G))
#print(sp[3]) #{3: [3], 1: [3, 1], 2: [3, 1, 2]}

import matplotlib.pyplot as plt

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3,
}

subax1 = plt.subplot(221)
nx.draw_random(G, **options)
subax2 = plt.subplot(222)
nx.draw_circular(G, **options)
subax3 = plt.subplot(223)
nx.draw_spectral(G, **options)
subax4 = plt.subplot(224)
nx.draw_shell(G, nlist=[range(5,10), range(5)], **options)


G = nx.dodecahedral_graph()
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
nx.draw_shell(G, nlist=shells, **options)
plt.show()

nx.draw(G)
plt.savefig("C://Users//zuhal//Desktop//bioinformaticProjects//final6//pict.png")


from networkx.drawing.nx_pydot import write_dot
pos = nx.nx_agraph.graphviz_layout(G)
nx.draw(G, pos=pos)
write_dot(G, 'C://Users//zuhal//Desktop//bioinformaticProjects//final6//file.dot')





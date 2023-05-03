import snap

""" 
İLK
Graph = snap.TNGraph.New();
Graph.AddNode(1);
Graph.AddNode(5);
Graph.AddNode(32);
Graph.AddEdge(1,5);
Graph.AddEdge(5,1);
Graph.AddEdge(5,32);

# Grafı networkx formatına dönüştürme

İLK
import networkx as nx
import matplotlib.pyplot as plt
G2 = nx.DiGraph()
for node in Graph.Nodes():
    G2.add_node(node.GetId())
for edge in Graph.Edges():
    G2.add_edge(edge.GetSrcNId(), edge.GetDstNId())
nx.draw(G2, with_labels=True)
plt.show()
"""
""" 
Graph= snap.GenRndGnm(snap.PNGraph,100,1000)

for NI in Graph.Nodes():
    print("node id %d with out-degree %d and in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))
for EI in Graph.Edges():
    print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
print("son")
for NI in Graph.Nodes():
    for e in NI.GetOutEdges():
        print("edge (%d %d)" % (NI.GetId(),e))
        
"""
""" 
Graph= snap.GenRndGnm(snap.PNGraph,100,1000)
print("İlk düğüm Id: %d " % (Graph.BegNI().GetId()))
print("Son düğüm  Id: %d " % (Graph.EndNI().GetId()))
ni1 = Graph.GetNI(1)
print("Düğüm 1 verisi:", ni1.GetData())
"""

""" 
Graph = snap.GenForestFire(1000, 0.35, 0.35)

# Ağ bilgilerini yazdırma
FOut = snap.TFOut("test.graph")
Graph.Save(FOut)
# Dosyadan grafı yükle
FIn = snap.TFIn("test.graph")
G2 = snap.TNGraph.Load(FIn)

# Grafı text dosyasına kaydet
snap.SaveEdgeList(Graph, "test.txt")
# Text dosyasından grafı yükle
G2 = snap.LoadEdgeList(snap.PNGraph, "test.txt", 0, 1)
"""

import snap
""" 
# Yeni bir graf oluştur
G = snap.GenForestFire(1000, 0.35, 0.35)
# Yönlü grafı yönsüz grafa dönüştür
UG = snap.ConvertGraph(snap.PUNGraph, G)
# En büyük bağlı bileşeni al
WccG = snap.GetMxWcc(G)
# {0,1,2,3,4,5} düğüm kümesine göre alt grafı al
SubG = snap.GetSubGraph(G, snap.TIntV.GetV(0, 1, 2, 3, 4))
# G'nin 3-core'unu al
Core3 = snap.GetKCore(G, 3)
# Derecesi 10 olan düğümleri sil
snap.DelDegKNodes(G, 10)


"""

# generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
G = snap.GenPrefAttach(1000, 3)
# get distribution of connected components (component size, count)
CntV = snap.TIntPrV()
snap.GetWccSzCnt(G, CntV)
# get degree distribution pairs (degree, count)
snap.GetOutDegCnt(G, CntV)
# get first eigenvector of graph adjacency matrix
EigV = snap.TFltV()
snap.GetEigVec(G, EigV)
# get diameter of G
snap.GetBfsFullDiam(G)
# count the number of triads in G, get the clustering coefficient of G
snap.GetTriads(G)
snap.GetClustCf(G)


""" 
G = snap.GenPrefAttach(1000, 3)
CntV = snap.TIntPrV()
snap.GetWccSzCnt(G, CntV)
snap.GetOutDegCnt(G, CntV)
EigV = snap.TFltV()
snap.GetEigVec(G, EigV)
snap.GetBfsFullDiam(G)
snap.GetTriads(G)
snap.GetClustCf(G)
"""

